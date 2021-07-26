from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import Profile

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100, help_text="Must be unique")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2', )