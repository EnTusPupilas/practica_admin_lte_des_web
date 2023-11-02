# forms.py
from django import forms
from .models import Menu, Client, Order

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'type', 'img']
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
