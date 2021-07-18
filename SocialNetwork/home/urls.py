from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signIn, name='signIn'),
    path('signIn/', views.signUp, name='signUp'),
]