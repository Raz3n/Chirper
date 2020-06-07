from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile
# Create your tests here.

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bang', password='apassword')
        self.user2 = User.objects.create_user(username='bing', password='apassword2')
        
    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)
    
    def test_following(self):
        first = self.user
        second = self.user2
        first.profile.followers.add(second)
        second_user_following_whom = second.following.all()
        qs = second_user_following_whom.filter(user = first)
        first_user_following_no_one = first.following.all()
        self.assertTrue(qs.exists())
        self.assertFalse(first_user_following_no_one.exists())