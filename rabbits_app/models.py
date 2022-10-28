from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from colorfield.fields import ColorField

class Rabbit(models.Model):
    user = models.ForeignKey(User,  default=None, on_delete=models.CASCADE)
    links = models.CharField(max_length=99999999)
    category = models.CharField(max_length=15)
    color = ColorField(default='#FF0000')
    date_created = models.DateTimeField(auto_now_add=True, blank=True)