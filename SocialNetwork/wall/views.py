from django.shortcuts import render
from home.views import getUser
from home.models import User

def index(request):
    context = {
        "user": getUser()
    }
    return render(request, "wall.html", context=context)
