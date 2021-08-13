from os import path
from django import urls
from django.conf.urls import url
from django.contrib import admin
from .views import profile_view, follow_view



urlpatterns = [
    url(r'^$',profile_view, name='user_profile'),
]