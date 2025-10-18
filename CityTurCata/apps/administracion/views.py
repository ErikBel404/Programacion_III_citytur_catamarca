from django.shortcuts import render
from django.http import HttpResponse

from apps.administracion.models import Transporte
from apps.administracion.models import Reportes

# Create your views here.

#Definicion de transporte
def listaTransportesView(request):
    #return render(request, 'administracion/transporte.html')   -> suponiendo que creamos una carpetea template dentro de la misma ponemos una carpeta administracion y dentro de ella tenemos el html de transporte
    return HttpResponse('Aca sale la lista de transportes');

def detalleTransporteView(request, id):
    return HttpResponse(f'Aca sale un transporte en detalle con id:{id}');

def registraTransporteView(request):
    return HttpResponse('Aca se registran los transportes solamente');

def modificarTransporteView(request):
    return HttpResponse('Aca se modifica el transporte');

#Definicion de reportes

def reportesView(request):
    return HttpResponse('Aca es la pagina de los resportes');

def reporteRecorridosActivosView(request):
    return HttpResponse('Aca va el reporte de recorridos activos');

def reporteParadasMasUtilizadasView(request):
    return HttpResponse('Aca van el reporte de las paradas mas utilizadas');

def reporteReservasRecorridoView(resquest):
    return HttpResponse('Aca va el reporte de las reservas de los recorridos');

def reporteConsultaReservas(request):
    return HttpResponse('Aca va el reporte de las consultas de las reservas');

def reporteEstadistaPasajeros(request):
    return HttpResponse('Aca va el reporte de estadisticas en un rango de fechas')

#Definicion de puntos Turisticos;

def PuntosTuristicosView(request):
    return HttpResponse('Aca es la pagina de los puntos turisticos')

def listarPuntosTuristicos(request):
    return HttpResponse('Aca iran los puntos turisticos y su informacion de actividad')

def CrearPuntosTuristicos(request):
    return HttpResponse('Aqui se solitara la informacion necesaria para crear los punto turisticos')



#Definicion de Recorridos;

def RecorridosView(request):
    return HttpResponse('Aca es la pagina de los Recorridos')

def listarRecorridos(request):
    return HttpResponse('Aca se mostrara una lista de los Recorridos')

def CrearRecorrido(request):
    return HttpResponse('Aqui se solicitara la informacion necesaria para crear un recorrido')

def modificarRecorridos(request):
    return HttpResponse('Aqui se mostrara la pagina de modificaciones')