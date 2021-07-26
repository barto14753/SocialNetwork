from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.BinaryField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'profile'

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveUserProfile(sender, instance, **kwargs):
    instance.profile.save()


