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
        
        widgets = { #para cuando haga el template mi shey

            'cantidadReserva': forms.TextInput(attrs={
                'class' : 'inputLaberl',
                'id': 'cantidadReservas'
            }),

            'fechaReserva': forms.DateInput(attrs = {
                'class':'inputLabel',
                'id':'fechaReserva' 
            }),

            'horaReserva':forms.TimeInput(attrs={
                'class':'inputLabel',
                'id': 'horaRerserva'
            }),

            'puntoDePartidaReserva': forms.CheckboxSelectMultiple(attrs={}),
            
            'estadoReserva':forms.Select(attrs={
                'class':'inputLabel',
                'id':'estatadoReserva'
            })
        }

        label={
            'cantidadReserva':'🚌 Cantidad de reservas',
            'fechaReserva': '📆 Fecha de la reserva',
            'horaReserva': '⌚ Hora de la reserva',
            'estadoReserva': '📋 Estado de la reserva'

        }