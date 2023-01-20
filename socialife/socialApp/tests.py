from urllib import response
from django.test import TestCase

# Create your tests here.
import json
from django.urls import reverse, reverse_lazy

from rest_framework.test import APIRequestFactory, APITestCase

from .model_factories import *
from .serializers import *

##########################user_test##########################
class UserTest(APITestCase):

    user1 = None
    user2 = None
    good_url = ''
    bad_url = ''

    def setUp(self):
        self.user1 = UserFactory.create(pk=1,  username = "tester")
        self.user2 = UserFactory.create(pk=2,  username = "tester2")
        self.good_url = reverse('user-api', kwargs={'pk': 1})
        self.bad_url = '/api/user/T/'

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_userReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('email' in data)
        self.assertEqual(data['email'], 'testing@email.com')

    def test_userReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    #(WONT TEST DELETE FOR USER AS WE DIDNT SET UP DELETE API)

class UserSerialiserTest(APITestCase):

    user1 = None
    userserialiser = None

    def setUp(self):
        self.user1 = UserFactory.create(pk=1,  username = "tester")
        self.userserialiser = UserSerializer(instance=self.user1)

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_userSerializer(self):
        data = self.userserialiser.data
        self.assertEqual(set(data.keys()), set(['username', 'email']))

    def test_userSerializerUsernameCorrect(self):
        data = self.userserialiser.data
        self.assertEqual(data['username'], 'tester')

    def test_userSerializerEmailCorrect(self):
        data = self.userserialiser.data
        self.assertEqual(data['email'], 'testing@email.com')

##########################appuser_test##########################
class AppUserTest(APITestCase):

    appuser1 = None
    appuser2 = None
    appuser3 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.appuser1 = AppUserFactory.create(pk=1,  user = UserFactory.create(pk=1,  username = "tester"))
        self.appuser2 = AppUserFactory.create(pk=2,  user = UserFactory.create(pk=2,  username = "tester2"))
        self.appuser3 = AppUserFactory.create(pk=3,  user = UserFactory.create(pk=3,  username = "tester3"))
        self.good_url = reverse('appuser-api', kwargs={'pk': 1})
        self.bad_url = '/api/appuser/A/'
        self.delete_url = reverse('appuser-api', kwargs={'pk': 3})

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_userReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('organisation' in data)
        self.assertEqual(data['organisation'], 'UOL')

    def test_userReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_userDeleteIsSuccesful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

class AppUserSerialiserTest(APITestCase):

    appuser1 = None
    appuserserialiser = None

    def setUp(self):
        self.appuser1 = AppUserFactory.create(pk=1,  user = UserFactory.create(pk=1,  username = "tester"))
        self.appuserserialiser = AppUserSerializer(instance=self.appuser1)

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_appuserSerializer(self):
        data = self.appuserserialiser.data
        self.assertEqual(set(data.keys()), set(['user', 'organisation']))

    def test_appuserSerializerUserCorrect(self):
        data = self.appuserserialiser.data
        self.assertEqual(data['user'], 1)

    def test_appuserSerializerOrganisationCorrect(self):
        data = self.appuserserialiser.data
        self.assertEqual(data['organisation'], 'UOL')

##########################profile_test##########################
class ProfileTest(APITestCase):

    profile1 = None
    profile2 = None
    profile3 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.profile1 = ProfileFactory.create(pk=1,  user = UserFactory.create(pk=1,  username = "tester"))
        self.profile2 = ProfileFactory.create(pk=2,  user = UserFactory.create(pk=2,  username = "tester2"))
        self.profile3 = ProfileFactory.create(pk=3,  user = UserFactory.create(pk=3,  username = "tester3"))
        self.good_url = reverse('profile-api', kwargs={'pk': 1})
        self.bad_url = '/api/profile/A/'
        self.delete_url = reverse('profile-api', kwargs={'pk': 3})

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_userReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('profile_image' in data)
        self.assertEqual(data['profile_image'], 'http://testserver/socialApp/image/profileImage/default.png')

    def test_userReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_userDeleteIsSuccesful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

class ProfileSerialiserTest(APITestCase):

    profile1 = None
    profileserialiser = None

    def setUp(self):
        self.profile1 = ProfileFactory.create(pk=1,  user = UserFactory.create(pk=1,  username = "tester"))
        self.profileserialiser = ProfileSerializer(instance=self.profile1)

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_profileSerializer(self):
        data = self.profileserialiser.data
        self.assertEqual(set(data.keys()), set(['user', 'name', 'bio', 'birthday', 'location', 'profile_image', 'friends']))

    def test_profileSerializerUserCorrect(self):
        data = self.profileserialiser.data
        self.assertEqual(data['user'], 1)

    def test_profileSerializerNameCorrect(self):
        data = self.profileserialiser.data
        self.assertEqual(data['name'], 'Shrek')

    def test_profileSerializerBioCorrect(self):
        data = self.profileserialiser.data
        self.assertEqual(data['bio'], 'Ogres are like Onions')

    def test_profileSerializerBirthdayCorrect(self):
        data = self.profileserialiser.data
        self.assertEqual(data['birthday'], '1999-02-27')

    def test_profileSerializerLocationCorrect(self):
        data = self.profileserialiser.data
        self.assertEqual(data['location'], 'Dreamworks')

    def test_profileSerializerProfileImageCorrect(self):
        data = self.profileserialiser.data
        self.assertEqual(data['profile_image'], 'http://testserver/socialApp/image/profileImage/default.png')

    def test_profileSerializerProfileImageCorrect(self):
        data = self.profileserialiser.data
        self.assertEqual(data['friends'], [])

##########################posts_test##########################
class PostsTest(APITestCase):

    post1 = None
    post2 = None
    post3 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.post1 = PostsFactory.create(pk=1,  publisher = UserFactory.create(pk=1,  username = "tester"))
        self.post2 = PostsFactory.create(pk=2,  publisher = UserFactory.create(pk=2,  username = "tester2"))
        self.post3 = PostsFactory.create(pk=3,  publisher = UserFactory.create(pk=3,  username = "tester3"))
        self.good_url = reverse('posts-api', kwargs={'pk': 1})
        self.bad_url = '/api/posts/A/'
        self.delete_url = reverse('posts-api', kwargs={'pk': 3})

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_userReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('image' in data)
        self.assertEqual(data['image'], None)

    def test_userReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_userDeleteIsSuccesful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

class PostsSerialiserTest(APITestCase):

    posts1 = None
    postsserialiser = None

    def setUp(self):
        self.posts1 = PostsFactory.create(pk=1,  publisher = UserFactory.create(pk=1,  username = "tester"))
        self.postsserialiser = PostsSerializer(instance=self.posts1)

    def tearDown(self):
        #after test, clear all created object in database and reset sequence
        User.objects.all().delete
        AppUser.objects.all().delete
        Profile.objects.all().delete
        Posts.objects.all().delete
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ProfileFactory.reset_sequence(0)
        PostsFactory.reset_sequence(0)

    def test_appuserSerializer(self):
        data = self.postsserialiser.data
        self.assertEqual(set(data.keys()), set(['status', 'created_on', 'publisher', 'image']))

    def test_appuserSerializerStatusCorrect(self):
        data = self.postsserialiser.data
        self.assertEqual(data['status'], "Onions have layers")

    def test_appuserSerializerCreated_OnCorrect(self):
        data = self.postsserialiser.data
        self.assertEqual(data['created_on'], '2022-08-29')

    def test_appuserSerializerPublisherCorrect(self):
        data = self.postsserialiser.data
        self.assertEqual(data['publisher'], 1)

    def test_appuserSerializerImageCorrect(self):
        data = self.postsserialiser.data
        self.assertEqual(data['image'], None)
