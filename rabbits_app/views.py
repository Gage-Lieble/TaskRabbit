from typing import final
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

        link_list_2 = [request.POST['site-1'],request.POST['site-2'],request.POST['site-3'],request.POST['site-4'],request.POST['site-5']] # Organized form data into list

        # Checks to see if any feilds empty
        final_links = ""
        for web in link_list_2:
            if web != '':
                final_links += f",{web}"
        
        if final_links[0] == ',':
                final_links = final_links[1:]
    
        new_rabbit = Rabbit(user=request.user, title=request.POST['title'], links=final_links)
        new_rabbit.save()
        return HttpResponseRedirect(reverse('users_app:interface'))

def edit_rabbit(request, name):
    if request.method == 'GET':
        model_data = Rabbit.objects.filter(title=name)

        for data in model_data:
            split_links = data.links.split(',')

                
        context = {
            'model_data': model_data,
            'links' : split_links
        }
        return render(request, 'rabbit_temps/editrabbit.html', context)
    elif request.method == 'POST':
        model_data = Rabbit.objects.get(title=name)
        model_data.title = request.POST['title']


        link_list = []
        for sitenum in request.POST:
            
            if sitenum[0] =='s':
                link_list.append(request.POST[sitenum])


        print(link_list)
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


def delete_rabbit(request, title):
        rabbit_begone = Rabbit.objects.filter(title=title)
       
        rabbit_begone.delete()
        return HttpResponseRedirect(reverse('users_app:interface'))
def emergency_button_wipe(request):
    Rabbit.objects.all().delete()
    return HttpResponseRedirect(reverse('users_app:index'))