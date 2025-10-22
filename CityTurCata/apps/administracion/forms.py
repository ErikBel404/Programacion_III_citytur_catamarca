from django import forms
from .models import PuntoTuristico

class PuntoTuristicoForm (forms.ModelForm):
    class Meta:
        model = PuntoTuristico
        fields = [
            'nombre',
            'ubicacion',
            'informacion'
            
        ]
        widgets = {
        }