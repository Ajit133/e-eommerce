from dataclasses import field
from unittest import mock
from django.forms import ModelForm
from .models import Profile,User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2',)
