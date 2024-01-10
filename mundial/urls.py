"""
URL configuration for mundial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from album import views
from restaurant import views
from post.api.router import router_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")), # new
    # path('selection/', views.SelectionListView.as_view(), name='selection-list'),
    # path('selection/<int:pk>/detail/', views.SelectionDetailView.as_view(), name='selection-detail'),
    # path('player/', views.PlayerListView.as_view(), name='player-list'),
    # path('player/<int:pk>/detail/', views.PlayerDetailView.as_view(), name='player-detail'),
    # # Update
    # path('player/<int:pk>/update/',views.PlayerUpdate.as_view(),name='player-update'), 
    # #Create
    # path('player/create/', views.PlayerCreate.as_view(), name='player-create'),
    # #Delete
    # path('player/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
    
    
    # #============================================================================   
    path('menu/', views.MenuListView.as_view(), name='menu-list'),
    path('menu/<int:pk>/update/', views.MenuUpdate.as_view(), name='menu-update'),
    # Update
    # path('menu/<int:pk>/update/',views.MenuUpdate.as_view(),name='menu-update'), 
    # #Create
    # path('menu/create/', views.MenuCreate.as_view(), name='menu-create'),
    # #Delete
    path('menu/<int:pk>/delete/', views.MenuDelete.as_view(), name='menu-delete'),
    path('menu/create/', views.MenuCreateView.as_view(), name='menu-create'),
    
    # #============================================================================   
    path('order/', views.OrderListView.as_view(), name='order-list'),
    # path('order/<int:pk>/detail/', views.OrderDetailView.as_view(), name='order-detail'),
    # # Update
    path('order/<int:pk>/update/',views.OrderUpdate.as_view(),name='order-update'), 
    # #Create
    # path('order/create/', views.OrderCreate.as_view(), name='order-create'),
    # #Delete
    path('order/<int:pk>/delete/', views.OrderDelete.as_view(), name='order-delete'),
    
    path('order/create/', views.OrderCreateView.as_view(), name='order-create'),
    
    # #============================================================================   
    path('client/', views.ClientListView.as_view(), name='client-list'),
    # path('client/<int:pk>/detail/', views.ClientDetailView.as_view(), name='client-detail'),
    # # Update
    path('client/<int:pk>/update/',views.ClientUpdate.as_view(),name='client-update'), 
    # #Create
    # path('client/create/', views.ClientCreate.as_view(), name='client-create'),
    # #Delete
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='client-delete'),
    path('client/create/', views.ClientCreateView.as_view(), name='client-create'),
    
    # #============================================================================   
    path('api/', include(router_posts.urls))
    
]
