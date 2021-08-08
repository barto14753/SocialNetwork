from django.contrib import admin
from django.http.response import FileResponse
from .models import Post, Like, Comment, Follow, Request, Friendship

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Request)
admin.site.register(Friendship)

