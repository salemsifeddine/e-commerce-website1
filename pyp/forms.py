from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.forms import ModelForm, fields, widgets
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *
username_validator = UnicodeUsernameValidator()



class CustomInfo(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                            widget=forms.EmailInput(attrs={'placeholder': 'Email',"class":"inpt",}),
                            )
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'placeholder': 'Password',})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}),
                                help_text=_('Just Enter the same password, for confirmation'))
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
   
   
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class signUp(UserCreationForm):
  
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

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




class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    password = forms.CharField(max_length=63,  widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    
    class Meta:
        model=User
        fields = ["username","password"]



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                            widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                            )
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'placeholder': 'Password',})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}),
                                help_text=_('Just Enter the same password, for confirmation'))
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)