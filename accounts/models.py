# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
        Clase que define un modelo de usuario personalizado en Django.
        
        Esta clase hereda del modelo AbstractUser de Django, proporcionando
        funcionalidades básicas de usuario. Puedes personalizar este modelo
        agregando campos adicionales o modificando su comportamiento según
        las necesidades específicas de tu aplicación.
    """
    pass