from django.db import models
from perfil.models  import Turista
from itinerarios.models  import Itinerario

# Create your models here.
class Reserva(models.Model):
    recorridoReserva = models.TextField(max_length=250, blank=False, null=False);
    cantidadReserva = models.IntegerField(blank=False, null=False);
    fechaReserva = models.DateField(blank=False, null=False);
    horaReserva = models.TimeField(blank=False, null=False);
    puntoDePartidaReserva = models.TextField(blank=False, null=False);
    estadoReseva = models.TextField(max_length=250, blank=False, null=False);

    turista= models.ForeignKey (Turista, on_delete= models.CASCADE, related_name='reservaTurista');
    itinerario= models.ForeignKey (Itinerario, on_delete=models.CASCADE, related_name='reservaitinerario')

    def __str__(self):
        return f'Recorrido de la reserva: {self.recorridoReserva}, cantidad de asientos reservados: {self.cantidadReserva}, fecha del recorrido: {self.fechaReserva}, hora de la reserva: {self.horaReserva}, punto de partida de persona:{self.puntoDePartidaReserva}, estado de la reserva: {self.estadoReseva}';
