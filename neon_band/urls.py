# neon_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('discography/', views.discography, name='discography'),
    path('tour/', views.tour, name='tour'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.user_profile, name='user_profile'),
]
