# pages/urls.py
from django.urls import path
from .views import HomePageView

"""
    Definición de la URL para la vista de la página de inicio.

    - '': Ruta raíz que se asocia a la clase HomePageView mediante el método as_view().
      El nombre 'home' se utiliza para referenciar esta URL en las plantillas.

"""
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
