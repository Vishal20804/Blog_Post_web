from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)


    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']