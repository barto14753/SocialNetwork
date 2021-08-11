from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from home.models import User
from home.views import getUser


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    print("Profile view got {0}".format(username))
    return render(request, 'profile.html', {'user': user})
