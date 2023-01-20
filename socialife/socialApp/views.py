from multiprocessing import context
import profile
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import *
from .models import *
from django.db.models import Q
#To authenticate users:
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

#initial landing page
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'social/index.html')

#View for home page
class HomePostsView(View):
    def get(self, request, *args, **kwargs):
        posts = Posts.objects.all().order_by('-created_on')
        form = PostsForm()
        context = {
            'home_post_list': posts,
            'form': form,
        }
        return render(request, 'social/home.html', context)
    def post(self, request, *args, **kwargs):
        posts = Posts.objects.all().order_by('-created_on')
        form = PostsForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.publisher = request.user
            new_post.save()

        context = {
            'home_post_list': posts,
            'form': form,
        }
        return render(request, 'social/home.html', context)

#Profile page
class UserProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Posts.objects.filter(publisher=user).order_by('-created_on')

        friends = profile.friends.all()

        if len(friends) == 0:
            is_a_friend = False
        
        for friend in friends:
            if friend == request.user:
                is_a_friend = True
                break
            else:
                is_a_friend = False

        total_friends = len(friends)
        
        context = {
            'profile': profile,
            'user': user,
            'posts': posts,
            'total_friends': total_friends,
            'is_a_friend': is_a_friend,
        }
        return render(request, 'social/profile.html', context)

#Search view
class SearchProfile(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = Profile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }
        return render(request, 'social/search.html', context)

#Chat index view
class ChatIndex(View):
    def get(self, request):
        return render(request, 'chat/index.html')

#Chatroom view
class ChatRoom(View):
    def get(self, request, room_name):
        loggedInUser = request.user.username
        context = {
            'room_name': room_name,
            'loggedInUser': loggedInUser
        }
        return render(request, 'chat/chatroom.html', context)

#To add friends
class AddFriend(View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.friends.add(request.user)

        return redirect('profile', pk=profile.pk)

#To remove friends
class RemoveFriend(View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.friends.remove(request.user)

        return redirect('profile', pk=profile.pk)

#To register users
def register(request):
    #initially false
    registered = False

    #User send us data
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'organisation' in user_form.cleaned_data:
                profile.organisation = request.DATA['organisation']
            profile.save()
            registered = True
    else: #if request.method is not 'POST' show user a blank form
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'authentication/register.html', {'user_form': user_form,
                                                          'profile_form': profile_form,
                                                          'registered': registered})

#To handle user logins
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            #if user is valid
            if user.is_active:
                #and user is active
                login(request, user)
                return HttpResponseRedirect('../home/')
            else:
                #if user is NOT active
                return HttpResponse('Your account is disabled')
        else:
            #if user is NOT valid
            return HttpResponse('Invalid login')
    else:
        return render(request, 'authentication/login.html')

#To logout
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('../')
