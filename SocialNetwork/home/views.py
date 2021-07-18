from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "title": "Social Network"
    }
    return render(request, "index.html", context=context)

def signIn(request):
    return render(request, "signIn.html")

def signUp(request):
    return render(request, "signUp.html")
