from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # URL for login, using custom view my_login
    path('', views.my_login, name='login'),
    # URL for logout, using custom view my_logout
    path('logout/', views.my_logout, name='logout'),
    # URL for registration, using custom view register
    path('registration/', views.register, name='registration'),
    # URL for home page
    path('home/', views.home, name='home'),
]