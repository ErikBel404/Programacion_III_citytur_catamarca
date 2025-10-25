from django.urls import path
from apps.administracion import views

app_name = 'administracion'

urlpatterns = [
    #urls de transporte
    path('transportes/lista/',views.listaTransportesView, name='listaTransporte'),
    path('transportes/agregar/',views.registraTransporteView, name='agregarTransporte'),
    path('transporte/modificar/<int:pk>/', views.modificarTransporteView, name='modificarTransporte'),
    path("transporte/baja/<int:pk>/", views.bajaTransporteView, name="bajaTransporte"),
    
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
    path('puntosTuristicos/agregar/', views.crearPuntosTuristicosView, name='agregaroPuntosTuristicos'),
    path('puntosTuristicos/modificar/<int:pk>/', views.modificarPuntoTuristicosView, name="modificarPuntosTuristicos"),
    path('puntosTuristicos/baja/<int:pk>/', views.bajaPuntoTuristicosView, name="bajaPuntosTuristico"),

    #
    #urls de recorridos
    path('recorridos/lista/', views.listarRecorridosView, name='ListarRecorridos'),
    path('recorridos/agregar/', views.crearRecorridosView, name='agregarRecorridos'),
    path('recorridos/modificar/', views.modificarRecorridosView, name='modificarRecorridos'),
    path('recorridos/baja/', views.bajaRecorridosView, name='bajaRecorridos'),

    #
    #urls de itinerarios
    path('itinerario/lista/', views.listarItinerarios, name='listarItinerarios'), 
    path('itinerario/agregar/', views.crearItinerarios , name='agregarItinerario'), 
    path('itinerario/modificar/', views.modificarItinerarios, name='modificarItinerarios'),
    path("itinenrario/baja/", views.bajaItinerarios, name="bajaItinerario"),

    #
    #urls de notificacion
    path('notificacion/lista/', views.listarNotificaciones , name='listarNotificaciones '), 
    path('notificacion/agregar/', views.crearNotificacion, name='agregarNotificacion'), 
    path('notificacion/modificar/', views.modificarNotificacion, name='modificarNotificacion'), 
    path('notificacion/baja/',views.bajaNotificacion,name='bajaNotificacion')
 
]
