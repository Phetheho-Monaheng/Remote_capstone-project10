from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('neon_band/', include('neon_band.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
