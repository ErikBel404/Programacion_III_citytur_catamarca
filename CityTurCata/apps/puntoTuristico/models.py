from django.db import models

# Create your models here.

class PuntoTuristico (models.Model):
    nombre = models.TextField(max_length=20)
    ubicacion = models.TextField(max_length=100)
    informacion = models.TextField(max_length=500)
    imagen = models.FileField()
    
    def __str__(self):
        return f'Nombre:{self.nombre} Ubicacion:{self.ubicacion} Informacion:{self.informacion} imagen:{self.imagen}'
