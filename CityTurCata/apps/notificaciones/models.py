from django.db import models
from perfil.models import Operario
from perfil.models import Administrador
from itinerarios.models import Itinerario


# Create your models here.
class Notificacion(models.Model):
    titulo=models.CharField(max_length=100, blank= False, null=False)
    descripcion=models.TextField(blank=False, null=False)

    operario= models.ForeignKey(Operario, on_delete=models.CASCADE, related_name='notificacionesOperario')
    administrador= models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='notificacionesAdministrador')
    itinerario= models.ForeignKey(Itinerario, on_delete=models.CASCADE, related_name='notificacionesItinerario')
    



    def __str__(self):
        return f'Titulo:{self.Titulo} Descripcion:{self.descripcion}'