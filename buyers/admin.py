from django.contrib import admin
from .models import Buyers

# Register your models here.

class BuyersAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name', 'email', 'location']

admin.site.register(Buyers, BuyersAdmin)