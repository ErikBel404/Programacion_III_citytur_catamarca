# En el archivo "forms.py" de tu aplicación

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Importa tu modelo

class RegistroUsuarioForm(UserCreationForm):
    
    # --- ¡AQUÍ ESTÁ LA CORRECCIÓN! ---
    # Los campos DEBEN llamarse 'password_1' y 'password_2'
    
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña', 
        widget=forms.PasswordInput
    )

    class Meta(UserCreationForm.Meta):
        model = Usuario
        
        # Campos de tu modelo que se pedirán
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'documento_identidad',
            'domicilio',
        ]
        
        # Etiquetas en español
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo Electrónico',
            'documento_identidad': 'Número de Documento',
            'domicilio': 'Domicilio',
        }