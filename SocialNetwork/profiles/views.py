from django.http.response import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from home.models import User
from home.views import getUser
from django.template import RequestContext
import json


def profile_view(request, username):
    user = request.user
    profile = get_object_or_404(User, username=username)
    posts = profile.get_my_posts()
    if not user.is_authenticated:
        return render(request, 'profile.html', context={'profile': profile})
    else:
        context = {
            'profile': profile,
            "friends": user.get_friends(),
            'is_followed': user.is_followed(profile),
            'is_friend': user.is_friend(profile),
            'is_requested': user.is_requested(profile),
            'am_i_requested': user.am_i_requested(profile),
            'posts': posts,
        }
        return render(request, 'profile.html', context=context)



def follow_view(request):
    if request.method == 'POST':
        user_username = request.user.username
        profile_username = request.POST.get('profile', None)
        user = get_object_or_404(User, username=user_username)
        profile = get_object_or_404(User, username=profile_username)

        user.follow(profile)
    
    context = {'followers': profile.followers}
    return HttpResponse(json.dumps(context), content_type='application/json')

    

def unfollow_view(request):
    if request.method == 'POST':
        user_username = request.user.username
        profile_username = request.POST.get('profile', None)
        user = get_object_or_404(User, username=user_username)
        profile = get_object_or_404(User, username=profile_username)

        user.unfollow(profile)
    
    context = {'followers': profile.followers}
    return HttpResponse(json.dumps(context), content_type='application/json')


def friend_handle_view(request, mode):
    if request.method == 'POST':
        user_username = request.user.username
        profile_username = request.POST.get('profile', None)
        user = get_object_or_404(User, username=user_username)
        profile = get_object_or_404(User, username=profile_username)

        if mode == "accept":
            user.accept_request(profile)
        elif mode == "send":
            user.send_request(profile)
        elif mode == "remove_request":
            user.remove_request(profile)
        elif mode == "remove_friend":
            user.remove_friend(profile)
        else:
            msg = "Wrong mode"
            return HttpResponseServerError(msg)
    
    context = {}
    return HttpResponse(json.dumps(context), content_type='application/json')



def send_request_view(request):
    return friend_handle_view(request, "send")

def remove_request_view(request):
    return friend_handle_view(request, "remove_request")

def accept_request_view(request):
    return friend_handle_view(request, "accept")

def remove_friend_view(request):
    return friend_handle_view(request, "remove_friend")


 
