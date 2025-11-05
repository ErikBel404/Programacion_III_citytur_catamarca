# En el archivo "forms.py" de tu aplicación

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  

class RegistroUsuarioForm(UserCreationForm):
    
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={
            'class': 'inputLabel',  
        })
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña', 
        widget=forms.PasswordInput(attrs={
            'class': 'inputLabel',  
        })
    )

    class Meta(UserCreationForm.Meta):
        model = Usuario 
        
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'documento_identidad',
            'domicilio',
        ]
        
       
        labels = {
            'username': '👤 Nombre de Usuario',
            'first_name': '🧑 Nombres',
            'last_name': '🧑 Apellidos',
            'email': '📧 Correo Electrónico',
            'documento_identidad': '🆔 Número de Documento',
            'domicilio': '🏠 Domicilio',
        }

        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'inputLabel',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'inputLabel',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'inputLabel',
            }),
            'email': forms.EmailInput(attrs={  
                'class': 'inputLabel',
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'inputLabel',
            }),
            'domicilio': forms.TextInput(attrs={
                'class': 'inputLabel',
            }),
        }
