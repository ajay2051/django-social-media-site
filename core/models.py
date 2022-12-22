from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


User = get_user_model()

# Create your models here.
class Profile(models.Model):
    id_user = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='uploads/', default='profile.png')
    location = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/',)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=200)
    username = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user


    
