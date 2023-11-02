from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    img = models.ImageField(upload_to='plate/')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('menu-list')
    
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    table = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('client-list')
    
class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.PROTECT,related_name='get_clients' )
    menu = models.ForeignKey('Menu', on_delete=models.PROTECT,related_name='get_menu' )
    total = models.IntegerField()
    amount = models.IntegerField()
    
    def __str__(self):
        return "Client: " + str(self.client) + " - Plate: " + str(self.menu) + " - Amount: " + str(self.amount)
    
    def get_absolute_url(self):
        return reverse('order-list')