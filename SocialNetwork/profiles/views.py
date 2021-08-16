from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from home.models import User
from home.views import getUser
from django.template import RequestContext


def profile_view(request, username):
    user = request.user
    profile = get_object_or_404(User, username=username)
    if not user.is_authenticated:
        return render(request, 'profile.html', context={'profile': profile})
    else:
        context = {
            'profile': profile,
            'is_followed': user.is_followed(profile),
            'is_friend': user.is_friend(profile),
            'is_requested': user.is_requested(profile),
            'am_i_requested': user.am_i_requested(profile),
        }
        return render(request, 'profile.html', context=context)

def follow_view(request, username):
    following = get_object_or_404(User, username=request.user.username)
    followed = get_object_or_404(User, username=username)
    following.follow(followed)
    return profile_view(request, username)

def unfollow_view(request, username):
    following = get_object_or_404(User, username=request.user.username)
    followed = get_object_or_404(User, username=request.profile.username)
    following.unfollow(followed)
    return profile_view(request, username)

def send_request_view(request, username):
    sender = get_object_or_404(User, username=request.user.username)
    receiver = get_object_or_404(User, username=request.profile.username)
    sender.send_request(receiver)
    return profile_view(request, username)

def remove_request_view(request, username):
    sender = get_object_or_404(User, username=request.user.username)
    receiver = get_object_or_404(User, username=request.profile.username)
    sender.delete_request(receiver)
    return profile_view(request, username)

def remove_friend_view(request, username):
    friend1 = get_object_or_404(User, username=request.user.username)
    friend2 = get_object_or_404(User, username=request.profile.username)
    friend1.remove_friend(friend2)
    return profile_view(request, username)



 
