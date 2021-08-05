from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="user_photos")

