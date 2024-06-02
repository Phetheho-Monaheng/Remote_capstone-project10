from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Band, Track, UserProfile, Review

# Register your models here

admin.site.register(Band)
admin.site.register(Track)
admin.site.register(UserProfile)
admin.site.register(Review)
