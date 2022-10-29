from django import forms
from django.forms import ModelForm
from .models import *


class CreateRabbitForm(forms.ModelForm):
    class Meta:
        model = Rabbit
        fields = '__all__'
        exclude = ['user', 'links']
        