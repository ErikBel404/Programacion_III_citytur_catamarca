from django.db import models

# Create your models here.
class Transporte(models.Model):
    dominioMatriculaTransporte = models.TextField(max_length=250, unique=True);
    capacidadTransporte = models.IntegerField(blank=False, null=False);
    estadoTransporte = models.TextField(max_length=250, blank= False, null= False);

    def __str__(self):
        return f'Matricula del Transporte: {self.dominioMatriculaTransporte}, Capacidad del transporte: {self.capacidadTransporte}, estado del Transporte: {self.estadoTransporte}'
    