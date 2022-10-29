from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# from colorfield.fields import ColorField


class Rabbit(models.Model):
    user = models.ForeignKey(User,  default=None, on_delete=models.CASCADE)
    links = models.CharField(max_length=999999)
    title = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user} - {self.title} - {self.links}"