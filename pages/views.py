from django.shortcuts import render
# pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """
        Vista de la página de inicio.

        Esta vista utiliza la clase TemplateView de Django para renderizar la página de inicio.
        El atributo 'template_name' especifica la plantilla HTML que se utilizará para renderizar
        esta vista.
    """
    template_name = "home.html"