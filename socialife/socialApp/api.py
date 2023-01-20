from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import *
from .serializers import *

##########################user_detail##########################
#View list of users
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Get only for user details
class UserDetails(mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

##########################appuser_detail##########################
#View list of appusers
class AppUserList(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

#Get/Post/Delete
class AppUserDetails(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#to update appuser
@api_view(['POST', 'GET'])
def update_appuser(request, pk):
    try:
        appuser = AppUser.objects.get(pk=pk)
    except AppUser.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = AppUserSerializer(appuser)
        return Response(serializer.data)
    else:
        serializer = AppUserSerializer(instance=appuser,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##########################profile_detail##########################
#View list of profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

#Get/Post/Delete
class ProfileDetails(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#to update profile
@api_view(['POST', 'GET'])
def update_profile(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    else:
        serializer = ProfileSerializer(instance=profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##########################posts_detail##########################
#View list of posts
class PostsList(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

#Get/Post/Delete
class PostsDetails(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
#to update posts
@api_view(['POST', 'GET'])
def update_posts(request, pk):
    try:
        posts = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PostsSerializer(posts)
        return Response(serializer.data)
    else:
        serializer = PostsSerializer(instance=posts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
