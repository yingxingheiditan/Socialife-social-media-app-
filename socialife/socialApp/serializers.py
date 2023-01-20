from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['user', 'organisation']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'bio', 'birthday', 'location', 'profile_image', 'friends']

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['status', 'created_on', 'publisher', 'image']
