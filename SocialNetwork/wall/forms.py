from django import forms
from .models import Post, Like, Comment



class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=300, widget=forms.Textarea)
    photo = forms.ImageField()


    class Meta:
        model = Post
        fields = ('content', 'photo')