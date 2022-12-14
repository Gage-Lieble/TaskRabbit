from django.urls import path
from . import views

app_name = 'users_app'
urlpatterns = [
    path('', views.index , name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('interface/', views.interface, name='interface'),
]