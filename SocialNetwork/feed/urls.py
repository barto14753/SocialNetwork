from django.conf.urls import url
from django.contrib import admin
from .views import like_view, unlike_view, comment_view



urlpatterns = [
    url(r'comment', comment_view, name='comment_url'),
    url(r'unlike', unlike_view, name='unlike_url'),
    url(r'like', like_view, name='like_url'),
]