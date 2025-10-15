from django.db import models
from transporte.models import Transporte
from recorridos.models import Recorrido
from reportes.models import Reportes 

# Create your models here.

class Itinerario(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    recorrido = models.TextField(blank=False, null=False)
    dominioTransporte = models.TextField(unique=True)

    transporte= models.ForeignKey(Transporte, on_delete=models.CASCADE, related_name='trasporteItinerario')
    recorridos= models.ForeignKey(Recorrido, on_delete=models.CASCADE, related_name='recorridoItinerario')
    reportes= models.ManyToManyField (Reportes, related_name='reportesNotificaciones')

    def __str__(self):
        return f'Titulo:{self.titulo} Descripcion:{self.descripcion} Recorrido:{self.recorrido} Dominio:{self.dominioTransporte}'