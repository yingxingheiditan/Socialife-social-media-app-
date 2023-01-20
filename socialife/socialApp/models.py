from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#models for user
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=256, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

#model for profiles
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete= models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='socialApp/image/profileImage', default='socialApp/image/profileImage/default.png', blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

#models for posts
class Posts(models.Model):
    status = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    publisher = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='socialApp/image/postImage', blank=True, null=True)
