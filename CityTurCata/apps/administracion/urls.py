from django.urls import path
from apps.administracion import views

from apps.administracion.views import crearItinerario, listarItinerarios, modificarItinerarios, buscarItinerarioParticular
from apps.administracion.views import crearNotificacion, listarNotificaciones, modificarNotificacion, buscarNotificacionParticular  

app_name = 'administracion'

urlpatterns = [
    #urls de transporte
    path('transportes/lista/',views.listaTransportesView, name='listaTransporte'),
    path('transportes/agregar/',views.registraTransporteView, name='registoTransporte'),
    path('transporte/modificar/', views.modificarTransporteView, name='modificarTransporte'),
    path("transporte/baja/", views.bajaTransporteView, name="bajaTransporte"),
    #
    #urls de reportes
    path('reportes/lista/',views.listaReportesView,name='listaReportes'),
    path('reportes/agregar/', views.reportesView, name='agregarReportes'),
    #
    path('reportes/activos/',views.reporteRecorridosActivosView, name='recorridosActivos'),
    path('reportes/paradas/',views.reporteParadasMasUtilizadasView,name ='paradasMasUtilizadas'),
    path('reportes/reservas/',views.reporteReservasRecorridoView, name= 'reservaRecorrido'),
    path('reportes/consultas/', views.reporteConsultaReservasView, name='consultasReservas'),
    path('reportes/estadisticas/', views.reporteEstadistaPasajerosView, name='estadisticasPasajeros'),
    #
    #urls de puntos Turisticos
    path('puntosTuristicos/lista/', views.listarPuntosTuristicosView, name='listaPuntosTuristicos'),
    path('puntosTuristicos/agregar/', views.crearPuntosTuristicosView, name='registroPuntosTuristicos'),
    path('puntosTuristicos/modificar', views.modificarPuntoTuristicosView, name="modificarPuntosTuristico"),
    path('puntosTuristicos/baja', views.bajaPuntoTuristicosView, name="bajaPuntosTuristico"),

    #
    #urls de recorridos
    path('recorridos/lista', views.listarRecorridosView, name='ListarRecorridos'),
    path('recorridos/agregar', views.crearRecorridosView, name='agregarRecorridos'),
    path('recorridos/modificar', views.modificarRecorridosView, name='modificarRecorridos'),
    path('recorridos/baja', views.bajaRecorridosView, name='bajaRecorridos'),

#----------- hasta aca toque yo no tocar mas de aca belicho

    #
    #urls de itinerarios
    path('itinerario', listarItinerarios, name='listarItinerarios'), 
    path('itinerario/crear', crearItinerario , name='crearItinerario'), 
    path('itinerario/modificar', modificarItinerarios, name='modificarItinerarios'), 
    path('itinerario/<int:id>',buscarItinerarioParticular , name='buscarItinerarioParticular'),
    #
    #urls de notificacion
    path('notificacion', listarNotificaciones , name='listarNotificaciones '), 
    path('notificacion/crear', crearNotificacion, name='crearNotificacion'), 
    path('notificacion/modificar', modificarNotificacion, name='modificarNotificacion'), 
    path('notificacion/<int:id>',buscarNotificacionParticular , name='buscarNotificacionParticular')
 
]
