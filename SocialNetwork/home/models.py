from django.db import models
from django.contrib.auth.models import AbstractUser
from wall.models import Follow, Friendship, Request, Post
from itertools import chain
from datetime import datetime


class User(AbstractUser):
    bio = models.TextField(max_length=500, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="user_photos")
    background = models.ImageField(null=True, blank=True, upload_to="user_backgrounds")
    joined = models.DateTimeField(default=datetime.now, blank=True)

    @property
    def followers(self):
        return len(Follow.objects.filter(followed=self))
    
    @property
    def following(self):
        return len(Follow.objects.filter(following=self))
    
    @property
    def friends(self):
        return len(Friendship.objects.filter(friend1=self)) + len(Friendship.objects.filter(friend2=self))
    
    @property
    def recived_requests(self):
        return len(Request.objects.filter(receiver=self))
    
    @property
    def sent_requests(self):
        return len(Request.objects.filter(sender=self))

    @property
    def posts(self):
        return len(Post.objects.filter(author=self))


    def get_followers(self):
        return Follow.objects.filter(followed=self)
    
    def get_following(self):
        return Follow.objects.filter(following=self)

    def get_friends(self):
        id1 = Friendship.objects.filter(friend2=self).values("friend1")
        id2 = Friendship.objects.filter(friend1=self).values("friend2")
        allIds = []

        for id1 in id1:
            allIds.append(id1["friend1"])
        for id2 in id2:
            allIds.append(id2["friend2"])
        
        # return query with user in alphabetical order
        return User.objects.filter(pk__in=allIds).order_by("username")
        

    def get_recived_requests(self):
        return Request.objects.filter(receiver=self)
    
    def get_sent_requests(self):
        return Request.objects.filter(sender=self)

    def get_posts(self):
        return Post.objects.filter(author=self)
    
    def send_request(self, receiver):
        if self is not receiver and not Request.objects.filter(sender=self, receiver=receiver).exists():
            Request.objects.create(sender=self, receiver=receiver)
    
    def remove_request(self, receiver):
        Request.objects.get(sender=self, receiver=receiver).delete()
    
    def follow(self, followed):
        if self is not followed and not Follow.objects.filter(following=self, followed=followed).exists():
            Follow.objects.create(following=self, followed=followed)
    
    def unfollow(self, followed):
        Follow.objects.get(following=self, followed=followed).delete()
    
    def accept_request(self, sender):
        sender.remove_request(self)
        if not Friendship.objects.filter(friend1=self, friend2=sender).exists():
            Friendship.objects.create(friend1=self, friend2=sender)
    
    def remove_friend(self, friend):
        if Friendship.objects.filter(friend1=self, friend2=friend).exists():
            Friendship.objects.filter(friend1=self, friend2=friend).delete()
        elif Friendship.objects.filter(friend1=friend, friend2=self).exists():
            Friendship.objects.get(friend1=friend, friend2=self).delete()
    
    def is_friend(self, other):
        return Friendship.objects.filter(friend1=self, friend2=other).exists() or Friendship.objects.filter(friend1=other, friend2=self).exists()

    def is_requested(self, other):
        return Request.objects.filter(sender=self, receiver=other).exists()
    
    def am_i_requested(self, other):
        return Request.objects.filter(sender=other, receiver=self).exists()
    
    def is_followed(self, other):
        return Follow.objects.filter(following=self, followed=other).exists()
    
    def am_i_followed(self, other):
        return Follow.objects.filter(following=other, followed=self).exists()

    
        

