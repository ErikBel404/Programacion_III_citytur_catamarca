from django.db import models
from apps.perfil.models import Administrador
from apps.perfil.models import Cliente
from apps.perfil.models import Operario

# Create your models here.
class Transporte(models.Model):

    ESTADOTRANSPORTE = [('activo', 'Activo'),
                        ('averiado','Averiado'),
                        ('reparacion','En Reparacion'),
                        ('fueraServicio', 'Fuera de Servicio')]

    dominioMatriculaTransporte = models.CharField(max_length=250, unique=True);
    capacidadTransporte = models.IntegerField(blank=False, null=False);
    estadoTransporte = models.CharField(max_length = 20, choices = ESTADOTRANSPORTE, default = 'activo', blank= False, null=False);

    administradores = models.ManyToManyField (Administrador, related_name= 'transportesAdministrador')

    def __str__(self):
        return f'Matricula del Transporte: {self.dominioMatriculaTransporte}, Capacidad del transporte: {self.capacidadTransporte}, estado del Transporte: {self.estadoTransporte}'
    
class Reportes(models.Model):
    TIPOINFORME=[('recoActivos', 'Recorridos Activos'),
                 ('paradasMasUtilizadas', 'Paradas Mas Utilizadas'),
                 ('reservaPorRecorrido','Reservas Por Recorrido'),
                 ('consultaDeReservas', 'Consulta De Reservas'),
                 ('estadisticasPasajeros', 'Estadisticas Pasajeros')
                 ]

    FORMATODOCUMENTO = [('pdf', 'PDF'),
                        ('excel', 'Excel'),
                        ('csv', 'CSV')]

    tipoReportes = models.CharField(max_length=40, blank=False, null=False, choices=TIPOINFORME, default='recoActivos');
    formatoReporte = models.CharField(max_length=20,blank=False, null=False, choices=FORMATODOCUMENTO, default='pdf')

    horaFecha= models.DateTimeField (blank=False, null= False);
    identidadSolicitante= models.CharField (blank=False, null= False, max_length=250)
    
    clientes= models.ManyToManyField (Cliente, related_name='reporteCliente');
    administradores= models.ManyToManyField (Administrador, related_name='reporteAdministrador');

    def __str__(self):
        return f'tipo de reporte: {self.tipoReportes}'
    
   
class PuntoTuristico (models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    ubicacion = models.CharField(max_length=100, blank=False, null=False)
    informacion = models.TextField(max_length=500, blank=False, null=False)
    imagen = models.ImageField(upload_to='puntos/', blank=True, null=True)

    administrador = models.ManyToManyField (Administrador, related_name= 'puntosTuristicosAdministrador')
    
    def __str__(self):
        return f'{self.nombre}'

    
class Recorrido (models.Model):
    
    nombreRecorrido = models.CharField(max_length=100, blank=False, null=False)
    horarios = models.TimeField(blank=False, null=False)

    inicio = models.CharField(max_length= 250, blank=False, null=False)
    final = models.CharField(max_length= 250, blank=False, null=False)

    administradores = models.ManyToManyField (Administrador, related_name= 'recorridosAdministrador')
    puntosTuristicos= models.ManyToManyField(PuntoTuristico, related_name='recorridosPuntosTuristicos')

    def __str__(self):
        return f'Nombre Recorrido: {self.nombreRecorrido} Horarios: {self.horarios} Puntos Turisticos: {self.puntosTuristicos} Inicio: {self.inicio} Fin: {self.final}'
 
class Itinerario(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)

    transporte= models.ForeignKey(Transporte, on_delete=models.CASCADE, related_name='trasporteItinerario')
    recorridos= models.ForeignKey(Recorrido, on_delete=models.CASCADE, related_name='recorridoItinerario')
    reportes= models.ManyToManyField (Reportes, related_name='reportesNotificaciones')

    def __str__(self):
        return f'Titulo:{self.titulo} Recorrido:{self.recorrido}'

class Notificacion(models.Model):
    titulo=models.CharField(max_length=100, blank= False, null=False)
    descripcion=models.TextField(blank=False, null=False)

    operario= models.ForeignKey(Operario, on_delete=models.CASCADE, related_name='notificacionesOperario',null=True, blank=True)
    administrador= models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='notificacionesAdministrador', null=True, blank=True)
    itinerario= models.ForeignKey(Itinerario, on_delete=models.CASCADE, related_name='notificacionesItinerario',null=True, blank=True)
    

    def __str__(self):
        return f'Titulo:{self.Titulo} Descripcion:{self.descripcion}'

