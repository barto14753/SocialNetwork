from os import path
from django import urls
from django.conf.urls import url
from django.contrib import admin
from .views import profile_view, follow_view, unfollow_view, send_request_view, accept_request_view, remove_friend_view, remove_request_view, reject_request_view



urlpatterns = [
    url(r'(?P<username>\w+)/', profile_view, name='user_profile'),
    url(r'follow', follow_view, name='follow_url'),
    url(r'unfollow', unfollow_view, name='unfollow_url'),
    url(r'send_request', send_request_view, name='send_request_url'),
    url(r'accept_request', accept_request_view, name='accept_request_url'),
    url(r'remove_request', remove_request_view, name='remove_request_url'),
    url(r'reject_request', reject_request_view, name='reject_request_url'),
    url(r'remove_friend', remove_friend_view, name='remove_friend_url'),
    
]