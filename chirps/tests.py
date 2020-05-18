from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Chirp

# Create your tests here.
User = get_user_model()

class ChirpTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='apassword')
        
    def test_chirp_created(self):
        chirp_obj = Chirp.objects.create(content="my chirp", user=self.user)
        self.assertEqual(chirp_obj.id, 1)
        self.assertEqual(chirp_obj.user, self.user)
        
    def test_api_login(self):
        client = APIClient()
        client.login(username=self.user.username, password='apassword')   