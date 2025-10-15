from django.db import models

# Create your models here.
class Recorrido (models.Model):
    nombreRecorrido = models.TimeField(max_length=100)
    horarios = models.TimeField()
    puntosTuristicos = models.TextField(max_length=200)
    inicio = models.TextField()
    final = models.TextField()

    def __str__(self):
        return f'Nombre Recorrido: {self.nombreRecorrido} Horarios: {self.horarios} Puntos Turisticos: {self.puntosTuristicos} Inicio: {self.inicio} Fin: {self.final}'