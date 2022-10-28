import re
from django.shortcuts import render

# Create your views here.

def create_rabbit(request):
    return render(request, 'rabbit_temps/createrabbit.html')

def edit_rabbit(request):
    return render(request, 'rabbit_temps/editrabbit.html')