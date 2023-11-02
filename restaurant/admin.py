from django.contrib import admin
from restaurant.models import Client, Order, Menu

# Register your models here.
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Menu)