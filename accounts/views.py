# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

"""
    Vista para la página de registro de usuarios.

    Esta vista utiliza la clase CreateView de Django para manejar la creación de nuevos
    usuarios. Se asocia al formulario CustomUserCreationForm para la entrada de datos
    del usuario. Después de un registro exitoso, redirige al usuario a la página de inicio
    de sesión ('login').
"""
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"