# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class CustomUserCreationForm(UserCreationForm):
    """
        Formulario de creación de usuario personalizado.

        Este formulario utiliza el modelo de usuario definido en la aplicación
        y especifica los campos requeridos para crear un nuevo usuario.

        Campos del formulario:
        - email: Dirección de correo electrónico del usuario.
        - username: Nombre de usuario del usuario.
    """
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

class CustomUserChangeForm(UserChangeForm):
    """
        Formulario de modificación de usuario personalizado.

        Este formulario utiliza el modelo de usuario definido en la aplicación
        y especifica los campos que se pueden modificar para un usuario existente.

        Campos del formulario:
        - email: Dirección de correo electrónico del usuario.
        - username: Nombre de usuario del usuario.
    """
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )