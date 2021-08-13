from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime



class Post(models.Model):
    author = models.ForeignKey("home.User", on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    published = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    photo = models.ImageField(null=True, blank=True, upload_to="post_photos")

    @property
    def likes(self):
        return len(Like.objects.filter(post=self))
    
    @property
    def comments(self):
        return len(Comment.objects.filter(post=self))
    
    def get_liking_users(self):
        return Like.objects.filter(post=self).values("user")
    
    def get_commenting_users(self):
        return Comment.objects.filter(post=self).values("user")
    
    def get_likes(self):
        return Like.objects.filter(post=self)
    
    def get_comments(self):
        return Comment.objects.filter(post=self)

    
class Like(models.Model):
    user = models.ForeignKey("home.User", on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    published = models.DateTimeField(default=datetime.now, blank=True)

class Comment(models.Model):
    user = models.ForeignKey("home.User", on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    content = models.CharField(max_length=200)
    published = models.DateTimeField(default=datetime.now, blank=True)

class Follow(models.Model):
    followed = models.ForeignKey("home.User", on_delete=CASCADE, related_name="followed")
    following = models.ForeignKey("home.User", on_delete=CASCADE)
    since = models.DateTimeField(default=datetime.now, blank=True)

class Request(models.Model):
    sender = models.ForeignKey("home.User", on_delete=CASCADE, related_name="sender")
    receiver = models.ForeignKey("home.User", on_delete=CASCADE)
    since = models.DateTimeField(default=datetime.now, blank=True)

class Friendship(models.Model):
    friend1 = models.ForeignKey("home.User", on_delete=CASCADE, related_name="friend1")
    friend2 = models.ForeignKey("home.User", on_delete=CASCADE)
    since = models.DateTimeField(default=datetime.now, blank=True)
