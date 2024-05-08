from django.contrib import admin
from .models import *

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )




admin.site.register(Listing, ListingAdmin)
admin.site.register(LikedListing)