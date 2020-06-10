import random
from django.conf import settings
from django.db import models
from django.db.models import Q


User = settings.AUTH_USER_MODEL

class ChirpLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey("Chirp", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class ChirpQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)
        
    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_user_id = []
        if profiles_exist:
            followed_user_id = user.following.values_list("user_id", flat=True)
        return self.filter(
            Q(user__id__in=followed_user_id) |
            Q(user=user)
        ).distinct().order_by("-timestamp")

class ChirpManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ChirpQuerySet(self.model, using=self._db)
    
    def feed(self, user):
        return self.get_queryset().feed(user)

class Chirp(models.Model):
    # id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL) # Chirp wont have a parent until it is rechirped
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chirps")
    likes = models.ManyToManyField(User, related_name='chirp_user', blank=True, through=ChirpLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ChirpManager()
    # def __str__(self): this would show the content of the chirp in the admin.
    #     return self.content
    
    class Meta:
        ordering = ['-id']
        
    @property
    def is_rechirp(self):
        return self.parent != None