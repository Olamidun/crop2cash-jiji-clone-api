from django.contrib import admin
from .models import Items

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name', 'image', 'price', 'seller', 'has_been_sold', 'sold_to']

admin.site.register(Items, ItemsAdmin)