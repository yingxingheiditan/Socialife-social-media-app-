from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import api

urlpatterns = [
    #landing page
    path('', Index.as_view(), name='index'),
    #authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #home
    path('home/', login_required(login_url='../login/')(HomePostsView.as_view()), name='home-post'),
    #profile
    path('profile/<int:pk>/', login_required(login_url='../login/')(UserProfileView.as_view()), name='profile'),
    path('profile/<int:pk>/friends/add/', login_required(login_url='../login/')(AddFriend.as_view()), name='add-friend'),
    path('profile/<int:pk>/friends/remove/', login_required(login_url='../login/')(RemoveFriend.as_view()), name='remove-friend'),
    #search
    path('search/', SearchProfile.as_view(), name='search-profile'),
    #chat
    path('chat/', login_required(login_url='../login/')(ChatIndex.as_view()), name='chat-index'),
    path('chat/<str:room_name>/', login_required(login_url='../login/')(ChatRoom.as_view()), name='chat-room'),
    #api: user
    path('api/user/', api.UserList.as_view(), name='user-api-list'),
    path('api/user/<int:pk>/', api.UserDetails.as_view(), name='user-api'),
    #api: appuser
    path('api/appuser/', api.AppUserList.as_view(), name='appuser-api-list'),
    path('api/appuser/<int:pk>/', api.AppUserDetails.as_view(), name='appuser-api'),
    path('api/appuser-update/<int:pk>/', api.update_appuser, name='appuser-api-update'),
    #api: profile
    path('api/profile/', api.ProfileList.as_view(), name='profile-api-list'),
    path('api/profile/<int:pk>/', api.ProfileDetails.as_view(), name='profile-api'),
    path('api/profile-update/<int:pk>/', api.update_profile, name='profile-api-update'),
    #api: posts
    path('api/posts/', api.PostsList.as_view(), name='posts-api-list'),
    path('api/posts/<int:pk>/', api.PostsDetails.as_view(), name='posts-api'),
    path('api/posts-update/<int:pk>/', api.update_posts, name='posts-api-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
