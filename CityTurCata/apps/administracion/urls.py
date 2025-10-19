from django.urls import path
from apps.administracion.views import listaTransportesView,detalleTransporteView,registraTransporteView,modificarTransporteView
from apps.administracion.views import reportesView,reporteRecorridosActivosView,reporteParadasMasUtilizadasView,reporteReservasRecorridoView,reporteConsultaReservas,reporteEstadistaPasajeros
from apps.administracion.views import PuntosTuristicosView,listarPuntosTuristicos,CrearPuntosTuristicos,RecorridosView,listarRecorridos,CrearRecorrido,modificarRecorridos
from apps.administracion.views import crearItinerario, listarItinerarios, modificarItinerarios, buscarItinerarioParticular
from apps.administracion.views import crearNotificacion, listarNotificaciones, modificarNotificacion, buscarNotificacionParticular  

app_name = 'administracion'
urlpatterns = [
    #urls de transporte
    path('transportes/',listaTransportesView, name='listaTransporte'),
    path('transportes/<int:id>/',detalleTransporteView, name='detalleTransporte'),
    path('transportes/agregar/',registraTransporteView, name='registoTransporte'),
    path('transporte/modificar/', modificarTransporteView, name='modificarTransporte'),
    #urls de reportes
    path('reportes/', reportesView, name='reportesTodos'),
    path('reportes/activos/',reporteRecorridosActivosView, name='recorridosActivos'),
    path('reportes/paradas/',reporteParadasMasUtilizadasView,name ='paradasMasUtilizadas'),
    path('reportes/reservas/',reporteReservasRecorridoView, name= 'reservaRecorrido'),
    path('reportes/consultas/', reporteConsultaReservas, name='consultasReservas'),
    path('reportes/estadisticas/', reporteEstadistaPasajeros, name='estadisticasPasajeros'),
    #urls de puntos Turisticos
    path('puntosTuristicos/', PuntosTuristicosView, name='puntosTuristicos'),
    path('puntosTuristicos/lista', listarPuntosTuristicos, name='listaPuntosTuristicos'),
    path('puntosTuristicos/crear', CrearPuntosTuristicos, name='crearPuntosTuristicos'),
    #urls de recorridos
    path('recorridos/', RecorridosView, name='paginaRecorridos'),
    path('recorridos/lista', listarRecorridos, name='ListarRecorridos'),
    path('recorridos/crear', CrearRecorrido, name='crearRecorridos'),
    path('recorridos/modificar', modificarRecorridos, name='modificarRecorridos'),
    #urls de itinerarios
    path('itinerario', listarItinerarios, name='listarItinerarios'), 
    path('itinerario/crear', crearItinerario , name='crearItinerario'), 
    path('itinerario/modificar', modificarItinerarios, name='modificarItinerarios'), 
    path('itinerario/<int:id>',buscarItinerarioParticular , name='buscarItinerarioParticular'),
    #urls de notificacion
    path('notificacion', listarNotificaciones , name='listarNotificaciones '), 
    path('notificacion/crear', crearNotificacion, name='crearNotificacion'), 
    path('notificacion/modificar', modificarNotificacion, name='modificarNotificacion'), 
    path('notificacion/<int:id>',buscarNotificacionParticular , name='buscarNotificacionParticular'),
]



