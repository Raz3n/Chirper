from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)