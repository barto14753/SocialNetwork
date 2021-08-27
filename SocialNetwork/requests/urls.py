from django.conf.urls import url
from django.contrib import admin
from .views import requests_view



urlpatterns = [
    url(r'', requests_view, name='requests_url'),
]