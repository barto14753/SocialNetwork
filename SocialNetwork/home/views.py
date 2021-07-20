from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "title": "Social Network"
    }
    return render(request, "index.html", context=context)

def register(request):
    return render(request, "registration/register.html")
