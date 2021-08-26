import json
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from home.models import User
from wall.models import Post

# Create your views here.

def unlike_view(request):
    if request.method == 'POST':
        user_username = request.user.username
        post_id = request.POST.get('post_id', None)
        user = get_object_or_404(User, username=user_username)
        post = get_object_or_404(Post, id=post_id)
        post.unlike(user)

        context = {'post_likes': post.likes}
        return HttpResponse(json.dumps(context), content_type='application/json')


def like_view(request):
    if request.method == 'POST':
        user_username = request.user.username
        post_id = request.POST.get('post_id', None)
        user = get_object_or_404(User, username=user_username)
        post = get_object_or_404(Post, id=post_id)

        post.like(user)

        context = {'post_likes': post.likes}
        return HttpResponse(json.dumps(context), content_type='application/json')


def comment_view(request):
    if request.method == 'POST':
        user_username = request.user.username
        post_id = request.POST.get('post_id', None)
        content = request.POST.get('content', None)
        user = get_object_or_404(User, username=user_username)
        post = get_object_or_404(Post, id=post_id)

        post.comment(user, content)
        context = {'post_comments': post.comments};
        return HttpResponse(json.dumps(context), content_type='application/json')

