from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Chirp

# Create your tests here.
User = get_user_model()

class ChirpTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='apassword')
        self.user2 = User.objects.create_user(username='cfe-2', password='apassword2')
        Chirp.objects.create(content="my first chirp", user=self.user)
        Chirp.objects.create(content="my first chirp", user=self.user)
        Chirp.objects.create(content="my first chirp", user=self.user2)
        self.current_count = Chirp.objects.all().count()
        
    def test_chirp_created(self):
        chirp_obj = Chirp.objects.create(content="my second chirp", user=self.user)
        self.assertEqual(chirp_obj.id, 4)
        self.assertEqual(chirp_obj.user, self.user)
        
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='apassword')
        return client
        
    def test_chirp_list(self):
        client = self.get_client()
        response = client.get("/api/chirps/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
    
    def test_chirps_related_name(self):
        user = self.user
        self.assertEqual(user.chirps.count(), 2)    
    
    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/chirps/action/", {"id": 1, "action": "like"})
        like_count = response.json().get("likes")
        user = self.user
        my_like_instances_count = user.chirplike_set.count()
        my_related_likes = user.chirp_user.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(like_count, 1)
        self.assertEqual(my_like_instances_count, 1)
        self.assertEqual(my_like_instances_count, my_related_likes)
        
    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/chirps/action/", {"id": 2, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/chirps/action/", {"id": 2, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)
        
    def test_action_rechirp(self):
        client = self.get_client()
        response = client.post("/api/chirps/action/", {"id": 2, "action": "rechirp"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_chirp_id = data.get("id")
        self.assertNotEqual(2, new_chirp_id)
        self.assertEqual(self.current_count + 1, new_chirp_id)
        
    def test_chirp_create_api_view(self):
        request_data = {"content": "This is my test chirp."}
        client = self.get_client()
        response = client.post("/api/chirps/create/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_chirp_id = response_data.get("id")
        self.assertEqual(self.current_count + 1, new_chirp_id)
        
    def test_chirp_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/chirps/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)
        
    def test_chirp_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/chirps/1/delete/")
        self.assertEqual(response.status_code, 200)
        client = self.get_client()
        response = client.delete("/api/chirps/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/chirps/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)
        
  