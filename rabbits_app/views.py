from ast import mod
from typing import final
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from guest_user.decorators import allow_guest_user
# Create your views here.

@allow_guest_user
def create_rabbit(request):
    if request.method == 'GET':
        form = CreateRabbitForm()
        context = {
            'form': form
        }
        return render(request, 'rabbit_temps/createrabbit.html', context)
    elif request.method == 'POST':

        link_list = [] # Organized form data into list
        print(len(request.POST)-2)
        for input in range(len(request.POST)-3): # Allows user to add as many sites as they want
            link_list.append(request.POST[f'site-{input+1}'])

        print(link_list)        
        # Checks to see if any feilds empty
        final_links = ""
        for web in link_list:
            if web != '':
                final_links += f",{web}"
        
        if final_links[0] == ',':
                final_links = final_links[1:]
    
        new_rabbit = Rabbit(user=request.user, title=request.POST['title'], links=final_links, color=request.POST['color'])
        new_rabbit.save()
        return HttpResponseRedirect(reverse('users_app:interface'))
@allow_guest_user
def edit_rabbit(request, name):
    if request.method == 'GET':
        model_data = Rabbit.objects.filter(title=name)

        for data in model_data:
            split_links = data.links.split(',')
        
        context = {
            'model_data': model_data,
            'links' : split_links,
            'color': model_data[0].color
        }
        return render(request, 'rabbit_temps/editrabbit.html', context)
    elif request.method == 'POST':

        print(request.POST)
        model_data = Rabbit.objects.get(title=name)
        model_data.title = request.POST['title']
        model_data.color = request.POST['color']

        link_list = []
        for sitenum in request.POST:
            
            if sitenum[0] =='s':
                link_list.append(request.POST[sitenum])


    
        # Checks to see if any feilds empty
        final_links = ""
        for web in link_list:
            if web != '':
                final_links += f",{web}"
        
        if final_links[0] == ',':
                final_links = final_links[1:]
    
        model_data.links = final_links

        model_data.save()
        return HttpResponseRedirect(reverse('users_app:interface'))

@allow_guest_user
def delete_rabbit(request, title):
        rabbit_begone = Rabbit.objects.filter(title=title)
       
        rabbit_begone.delete()
        return HttpResponseRedirect(reverse('users_app:interface'))

def emergency_button_wipe(request):
    Rabbit.objects.all().delete()
    return HttpResponseRedirect(reverse('users_app:index'))