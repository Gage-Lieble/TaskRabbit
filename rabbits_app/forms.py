from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import TextInput

class CreateRabbitForm(forms.ModelForm):
    class Meta:
        model = Rabbit
        fields = '__all__'
        exclude = ['user', 'links']
        widgets ={
           
            'color': TextInput(attrs={'type':'color'}),

            }