from asyncio.windows_events import NULL
import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from .models import *

class UserFactory(factory.django.DjangoModelFactory):
    username = "tester1"
    email = "testing@email.com"

    class Meta:
        model = User

class AppUserFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    organisation = "UOL"

    class Meta:
        model = AppUser

class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    name = "Shrek"
    bio = "Ogres are like Onions"
    birthday = "1999-02-27"
    location = "Dreamworks"
    #did not initialise profile_image to check if default image is set
    #did not set friends field (will return empty list [])

    class Meta:
        model = Profile

class PostsFactory(factory.django.DjangoModelFactory):
    status = "Onions have layers"
    created_on = "2022-08-29"
    publisher = factory.SubFactory(UserFactory)
    image = None

    class Meta:
        model = Posts
