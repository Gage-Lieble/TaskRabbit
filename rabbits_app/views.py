from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def create_rabbit(request):
    if request.method == 'GET':
        form = CreateRabbitForm()
        context = {
            'form': form
        }
        return render(request, 'rabbit_temps/createrabbit.html', context)
    elif request.method == 'POST':
        new_rabbit = Rabbit(user=request.user, title=request.POST['title'], links=request.POST['links'])
        new_rabbit.save()
        return HttpResponseRedirect(reverse('users_app:interface'))

def edit_rabbit(request, name):
    if request.method == 'GET':
        model_data = Rabbit.objects.filter(title=name)
        context = {
            'model_data': model_data
        }
        return render(request, 'rabbit_temps/editrabbit.html', context)
    elif request.method == 'POST':
        model_data = Rabbit.objects.get(title=name)
        model_data.title = request.POST['title']
        model_data.links = request.POST['links']
        model_data.save()
        return HttpResponseRedirect(reverse('users_app:interface'))
