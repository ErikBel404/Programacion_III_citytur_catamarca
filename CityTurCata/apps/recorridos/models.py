from django.db import models
from perfil.models import Administrador
from puntoTuristico.models import PuntoTuristico

# Create your models here.
class Recorrido (models.Model):
    nombreRecorrido = models.TimeField(max_length=100, blank=False, null=False)
    horarios = models.TimeField(blank=False, null=False)
    puntosTuristicos = models.TextField(max_length=200, blank=False, null=False)
    inicio = models.TextField(max_length= 250, blank=False, null=False)
    final = models.TextField(max_length= 250, blank=False, null=False)

    administradores = models.ManyToManyField (Administrador, related_name= 'recorridosAdministrador')
    puntosTuristicos= models.ManyToManyField(PuntoTuristico, related_name='recorridosPuntosTuristicos')

    def __str__(self):
        return f'Nombre Recorrido: {self.nombreRecorrido} Horarios: {self.horarios} Puntos Turisticos: {self.puntosTuristicos} Inicio: {self.inicio} Fin: {self.final}'