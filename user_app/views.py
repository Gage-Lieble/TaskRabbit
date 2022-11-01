from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rabbits_app.models import *
# Create your views here.
from guest_user.decorators import allow_guest_user

# @allow_guest_user
def index(request):
    
    return render(request, 'base_temps/index.html', )

@allow_guest_user
def interface(request):
    rabbits_model = Rabbit.objects.filter(user=request.user)
    rabbits = {}
    for index, link_list in enumerate(rabbits_model):
        conversion = rabbits_model[index].links.split(',')
        rabbits[rabbits_model[index].title] = [conversion, rabbits_model[index].color]
        
    
    context = {
        "rabbit_list": rabbits
    }

    return render(request, 'base_temps/interface.html', context)


def signup(request):
    if request.method == 'GET':
        sign_form = SignupForm()
        context = {
        'sign_form': sign_form
        }
        return render(request, 'base_temps/signup.html', context)

    elif request.method == 'POST':
        form_data = SignupForm(request.POST)

        if form_data.is_valid():
            new_user = User.objects.create_user(
                username = form_data.cleaned_data['username'],
                password = form_data.cleaned_data['password'],
                email = form_data.cleaned_data['email']
            )
            sign_user = authenticate(username=form_data.cleaned_data['username'], password=form_data.cleaned_data['password'])
            login(request, new_user)
    return HttpResponseRedirect(reverse('users_app:interface'))

def user_login(request):
    if request.method == 'GET':
        log_form = LoginForm()
        context = {
            'log_form': log_form
        }
        return render(request, 'base_temps/login.html', context)
    elif request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            password = log_form.cleaned_data['password']
            username = log_form.cleaned_data['username']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('users_app:interface'))
            else:
                # Checks if user exists
                log_form.add_error('username', 'Invalid email or password')
                return render(request, 'base_temps/login.html', {'log_form': log_form})

    return render(request, 'base_temps/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users_app:index'))