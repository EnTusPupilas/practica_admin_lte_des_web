# accounts/urls.py
from django.urls import path
from .views import SignupPageView

"""
    Definición de las URL para las vistas relacionadas con la gestión de cuentas de usuario.
"""
urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]