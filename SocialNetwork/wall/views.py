from .models import Post
from django.shortcuts import render
from home.views import getUser
from home.models import User
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    user = getUser(request)

    context = {
        "user": user,
        "form": PostForm()
    }
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_new = form.save(commit=False)
            post_new.author = user
            post_new.save()

    return render(request, "wall.html", context=context)
