from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from home.forms import SignUpForm

context = {
    "user": None
}

def getUser():
    return context["user"]

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/wall')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def log(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        context["user"] = user
        print(user.last_login)
        if user is not None:
            login(request, user)
            print(getUser())
            return redirect('/wall')
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            pass
    else:
        pass
    return render(request, 'registration/login.html')

def index(request):
    context = {
        "title": "Social Network"
    }
    return render(request, "index.html", context=context)

