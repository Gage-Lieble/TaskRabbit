from django import forms
from django.forms import ModelForm
from .models import *

class SignupForm(forms.Form):
    username = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='', max_length=10,)
    
class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'placeholder': ' Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' Your Password'}), label='', max_length=10,)
