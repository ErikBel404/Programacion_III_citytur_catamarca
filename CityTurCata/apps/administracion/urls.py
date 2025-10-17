from django.urls import path
from apps.administracion.views import listaTransportesView,detalleTransporteView,registraTransporteView,modificarTransporteView
from apps.administracion.views import reportesView,reporteRecorridosActivosView,reporteParadasMasUtilizadasView,reporteReservasRecorridoView,reporteConsultaReservas,reporteEstadistaPasajeros

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
    path('reportes/estadisticas/', reporteEstadistaPasajeros, name='estadisticasPasajeros')

]
