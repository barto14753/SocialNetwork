from django.db import models
from django.contrib.auth.models import AbstractUser
from wall.models import Follow, Friendship, Request
from itertools import chain

class User(AbstractUser):
    bio = models.TextField(max_length=500, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="user_photos")

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


    def get_followers(self):
        return Follow.objects.filter(followed=self)
    
    def get_following(self):
        return Follow.objects.filter(following=self)

    def get_friends(self):
        q1 = Friendship.objects.filter(friend1=self).values("friend2")
        q2 = Friendship.objects.filter(friend2=self).values("friend1")

        return list(chain(q1, q2))

    def get_recived_requests(self):
        return Request.objects.filter(receiver=self)
    
    def get_sent_requests(self):
        return Request.objects.filter(sender=self)
    

    
        

