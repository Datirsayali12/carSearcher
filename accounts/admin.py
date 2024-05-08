from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number','bio')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','address1','city','state')
