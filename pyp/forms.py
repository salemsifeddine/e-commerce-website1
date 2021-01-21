from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class CustomInfo(UserCreationForm):
   
    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"email"
    }))
    
    
    class Meta:
        model=User
        fields=["username","email"]



class Photoprofile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["image"]

class ImagePro(forms.ModelForm):
    class Meta:
        model=Product
        fields=["name","description","new_price","old_price","catigory","rate","image"]
        