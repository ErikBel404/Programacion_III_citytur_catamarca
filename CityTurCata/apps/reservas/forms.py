from django import forms
from apps.reservas.models import Reserva
from apps.administracion.models import Recorrido

class ReservaForm(forms.ModelForm):
    
    recorridoReserva = forms.ModelChoiceField(
        queryset=Recorrido.objects.all(),
        required=True,
        label='🛣️ Recorridos Disponibles para reservar',
        empty_label='',
        widget=forms.Select(attrs={
            'class': 'inputLabel',
            'id': 'recorridos',
            'requiered': True
        })
    )
    
    
    class Meta:
        model = Reserva
        fields = ['recorridoReserva',
                  'cantidadReserva',
                  'fechaReserva',
                  'horaReserva',
                  'puntoDePartidaReserva',
                  'estadoReserva',
                  'itinerario']
        
        widgets = { 
            'cantidadReserva': forms.TextInput(attrs={
                'class' : 'inputLabel',
                'id': 'cantidadReservas',
                'required': True,
                'placeholder': ' '

            }),

            'fechaReserva': forms.DateInput(attrs = {
                'class':'inputLabel',
                'id':'fechaReserva',
                'required': True,
                'type':'date'

            }),

            'horaReserva':forms.TimeInput(attrs={
                'class':'inputLabel',
                'id': 'horaRerserva',
                'required': True,
                'type': 'time',
                'placeholder': ' ' 


            }),

            'puntoDePartidaReserva': forms.CheckboxSelectMultiple(attrs={
                'required': True,
                'placeholder': ' '

            }),
            
            'estadoReserva':forms.Select(attrs={
                'class':'inputLabel',
                'id':'estatadoReserva',
                'placeholder': ' '
            })
        }

        labels = {
            'cantidadReserva':'🚌 Cantidad de reservas',
            'fechaReserva': '📆 Fecha de la reserva',
            'horaReserva': '⌚ Hora de la reserva',
            'estadoReserva': '📋 Estado de la reserva',
            'puntoDePartidaReserva':'🚏 Punto de partida Reserva'

        }