from django import forms
from django.forms import ModelForm, ImageField
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ('organisation', )

class PostsForm(forms.ModelForm):
    #customize the status field
    status = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Post Something...'
        })
    )

    image = ImageField(required=False)
    
    class Meta:
        model = Posts
        fields = ['status', 'image']
