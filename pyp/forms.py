from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields, widgets
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

class EmailField(forms.ModelForm):
    class Meta:
        model=NewsLetterEmails
        fields="__all__"

class SearchForm(forms.ModelForm):
    class Meta:
        model=SearchItem
        fields=("query",)

class ShippingForm(forms.ModelForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder":"Email..",
        
    }))

    address=forms.CharField(widget=forms.TextInput(attrs={
       
        "placeholder":"Address..",
        "id":"address",
        "name":"address"
    }))
    city=forms.CharField(widget=forms.TextInput(attrs={
       
        "placeholder":"City..",
        "id":"city"
    }))
    state=forms.CharField(widget=forms.TextInput(attrs={
       
        "placeholder":"State..",
         "id":"state"
    }))
    zip_code1= forms.IntegerField(widget=forms.NumberInput(attrs={
         "placeholder":"Zip Code..",
         "id":"zip"
    }))
    zip_code2= forms.IntegerField(widget=forms.NumberInput(attrs={
         "placeholder":"Zip Code..",
         "id":"zip2"
    }))
    
    class Meta:
        model=ShippingAddress
        fields=["email","address","city","state","zip_code1","zip_code2"]

        