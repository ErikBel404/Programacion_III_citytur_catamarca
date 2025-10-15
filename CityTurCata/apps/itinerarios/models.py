from django.db import models

# Create your models here.

class Itinerario(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    recorrido = models.TextField(blank=True)
    dominioTransporte = models.TextField(blank=True)

    def __str__(self):
        return f'Titulo:{self.titulo} Descripcion:{self.descripcion} Recorrido:{self.recorrido} Dominio:{self.dominioTransporte}'