from django.contrib import admin
from .models import Reserva

@admin.register (Reserva)
class ReservaAdmin (admin.ModelAdmin):
    list_display=['recorridoReserva', 'cantidadReserva', 'fechaReserva', 'horaReserva', 'puntoDePartidaReserva', 'estadoReserva', 'turista', 'itinerario']

# Register your models here.
