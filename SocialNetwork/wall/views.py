from django.shortcuts import render
from home.views import getUser

def index(request):
    print(getUser())
    context = {
        "user": getUser()
    }
    return render(request, "wall.html", context=context)
