from django.db import models

# Create your models here.
class Notificacion(models.Model):
    Titulo=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return f'Titulo:{self.Titulo} Descripcion:{self.descripcion}'