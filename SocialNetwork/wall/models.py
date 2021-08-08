from django.db import models
from django.db.models.deletion import CASCADE
from home.models import User
from datetime import datetime    


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    published = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    photo = models.ImageField(null=True, blank=True, upload_to="post_photos")

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    published = models.DateTimeField(default=datetime.now, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    content = models.CharField(max_length=200)
    published = models.DateTimeField(default=datetime.now, blank=True)

class Follow(models.Model):
    followed = models.ForeignKey(User, on_delete=CASCADE, related_name="followed")
    following = models.ForeignKey(User, on_delete=CASCADE)
    since = models.DateTimeField(default=datetime.now, blank=True)

class Request(models.Model):
    sender = models.ForeignKey(User, on_delete=CASCADE, related_name="sender")
    reciver = models.ForeignKey(User, on_delete=CASCADE)
    since = models.DateTimeField(default=datetime.now, blank=True)

class Friendship(models.Model):
    friend1 = models.ForeignKey(User, on_delete=CASCADE, related_name="friend1")
    friend2 = models.ForeignKey(User, on_delete=CASCADE)
    since = models.DateTimeField(default=datetime.now, blank=True)
