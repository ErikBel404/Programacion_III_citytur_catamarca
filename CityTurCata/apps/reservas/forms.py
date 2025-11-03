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

        }

        label={

        }