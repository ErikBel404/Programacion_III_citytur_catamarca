from django.db import models
from perfil.models import Administrador

# Create your models here.

class PuntoTuristico (models.Model):
    nombre = models.TextField(max_length=20, blank=False, null=False)
    ubicacion = models.TextField(max_length=100, blank=False, null=False)
    informacion = models.TextField(max_length=500, blank=False, null=False)
    imagen = models.FileField()

    administrador = models.ManyToManyField (Administrador, related_name= 'puntosTuristicosAdministrador')
    
    def __str__(self):
        return f'Nombre:{self.nombre} Ubicacion:{self.ubicacion} Informacion:{self.informacion} imagen:{self.imagen}'
