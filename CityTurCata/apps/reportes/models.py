from django.db import models
from perfil.models import Cliente
from perfil.models import Administrador

# Create your models here.
class Reportes(models.Model):
    tipoReportes = models.TextField(max_length=250, blank=False, null=False);
    horaFecha= models.DateTimeField (blank=False, null= False);
    identidadSolicitante= models.TextField (blank=False, null= False)
    
    clientes= models.ManyToManyField (Cliente, related_name='reporteCliente');
    administradores= models.ManyToManyField (Administrador, related_name='reporteAdministrador');

    def __str__(self):
        return f'Descripcion del reporte: {self.descripcionReportes}, tipo de reporte: {self.tipoReportes}'