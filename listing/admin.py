"""Module for Admin functions"""
from django.contrib import admin
from .models import Interest, Listings
# Register your models here.
admin.site.register(Listings)


class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

admin.site.register(Interest, InterestAdmin)

  
  