from django.db import models
from apps.perfil.models  import Turista
from apps.administracion.models  import Itinerario
from apps.administracion.models import PuntoTuristico, Recorrido

# Create your models here.
class Reserva(models.Model):
    recorridoReserva = models.ForeignKey (Recorrido, on_delete= models.CASCADE, related_name='reservaTurista', blank=True, null= True);
    cantidadReserva = models.IntegerField(blank=False, null=False);
    fechaReserva = models.DateField(blank=False, null=False);
    horaReserva = models.TimeField(blank=False, null=False);

    puntoDePartidaReserva = models.ManyToManyField(PuntoTuristico, related_name = 'puntosDePartida', blank = False)
    
    ESTADORESERVA=[('reservaActiva','Reserva Activa'),
                   ('reservaCancelada','Reserva Cancelada')]

    estadoReserva = models.CharField(max_length=250, blank=False, null=False, choices=ESTADORESERVA, default='reservaActiva');

    turista= models.ForeignKey (Turista, on_delete= models.CASCADE, related_name='reservaTurista', blank=True, null= True);
    itinerario= models.ForeignKey (Itinerario, on_delete=models.CASCADE, related_name='reservaitinerario', blank=True, null= True)

    def __str__(self):
        return f'Recorrido: {self.recorridoReserva}, Cantidad: {self.cantidadReserva}, Fecha: {self.fechaReserva}, Estado: {self.estadoReserva}';