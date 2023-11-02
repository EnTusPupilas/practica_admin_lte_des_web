from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from restaurant.models import Client, Menu, Order

from .forms import MenuForm, ClientForm, OrderForm
# Create your views here.
#============================================================================    
#CLIENT
class ClientListView(ListView):
    model = Client
    
class ClientDetailView(DetailView):
    model = Client
    
class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__' 

class ClientCreate(CreateView):
    model = Client
    fields = '__all__'

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client-list')
    
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'restaurant/client_create.html'  # Asegúrate de tener el nombre correcto de tu plantilla
    success_url = reverse_lazy('client-list')
    
#============================================================================  
# MENU
class MenuListView(ListView):
    model = Menu
    
class MenuDetailView(DetailView):
    model = Menu
    
class MenuUpdate(UpdateView):
    model = Menu
    fields = '__all__' 

class MenuDelete(DeleteView):
    model = Menu
    success_url = reverse_lazy('menu-list')
    
class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'restaurant/menu_create.html'  # Asegúrate de tener el nombre correcto de tu plantilla
    success_url = reverse_lazy('menu-list')
    
#============================================================================  
# ORDER
class OrderListView(ListView):
    model = Order
    
class OrderDetailView(DetailView):
    model = Order
    
class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__' 

class OrderCreate(CreateView):
    model = Order
    fields = '__all__'

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')
    
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'restaurant/order_create.html'  # Asegúrate de tener el nombre correcto de tu plantilla
    success_url = reverse_lazy('order-list')