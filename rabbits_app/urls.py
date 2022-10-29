
from django.urls import path
from . import views

app_name = 'rabbits_app'
urlpatterns = [
    path('create/', views.create_rabbit, name='create_rabbit'),
    path('edit/<str:name>', views.edit_rabbit, name='edit_rabbit'),
 
]
