from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# from post.models import Post

User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='default-user-profile.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

# Uploading Post


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    # upload_time = models.DateTimeField(auto_now_add=True)
    # no_of_shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user


# Like Post
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# Follower's Count
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
# Help_Centre


class HelpCentre(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    msgcontent=models.TextField()

    def __str__(self):
        return self.fullname

# Share Post


# class SharedPost(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     original_post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     shared_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username} - {self.shared_at}'


class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)
