from django.contrib import admin
from .models import Transporte, PuntoTuristico, Recorrido, Itinerario, Notificacion

# Register your models here.
@admin.register (Transporte)
class TransporteAdmin (admin.ModelAdmin):
    list_display = [ 'dominioMatriculaTransporte', 'capacidadTransporte', 'estadoTransporte']
    
    
    
#@admin.register (Reportes)
#class ReportesAdmin (admin.ModelAdmin):
#    list_display = ['tipoReportes', 'formatoReporte', 'horaFecha', 'identidadSolicitante' ]
    
@admin.register (PuntoTuristico)
class PuntoTuristicoAdmin (admin.ModelAdmin):
    list_display=['nombre', 'ubicacion', 'informacion', 'imagen']


@admin.register (Recorrido)
class RecorridoAdmin (admin.ModelAdmin):
    list_display=['nombreRecorrido', 'horarios','inicio', 'final']
    
    
@admin.register (Itinerario)
class ItinerarioAdmin (admin.ModelAdmin):
    list_display= ['titulo', 'transporte', 'recorridos' ]

@admin.register (Notificacion)
class NotificacionAdmin (admin.ModelAdmin):
    list_display =['titulo', 'descripcion','activo_en_home','operario', 'administrador', 'itinerario']