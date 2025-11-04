from django import forms
from apps.reservas.models import Reserva

class ReservaForm(forms.ModelForm):
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
            #'recorridoReserva',

            'cantidadReserva': forms.TextInput(attrs={
                'class' : 'inputLaberl',
                'id': 'cantidadReservas'
            }),

            'fechaReserva': forms.DateInput(attrs = {
                'class':'inputLabel',
                'id':'fechaReserva' 
            }),

            'horaReserva':forms.TimeInpout(attrs={
                'class':'inputLabel',
                'id': 'horaRerserva'
            }),
            
            'estadoReserva':forms.Select(attrs={
                'class':'inputLabel',
                'id':'estatadoReserva'
            })
        }

        label={
            'cantidadReserva':'🚌 Cantidad de reservas',
            'fechaReserva': '📆 Fecha de la reserva',
            


        }