from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

##importaciones de los modelos
from apps.administracion.models import Transporte
from apps.administracion.models import Reportes

#importaciones de los form
from .forms import PuntoTuristicoForm
from .forms import TransporteForm, ReportesForm

# Create your views here.

#Definicion de transporte
def listaTransportesView(request):
    #return render(request, 'administracion/transporte.html')   -> suponiendo que creamos una carpetea template dentro de la misma ponemos una carpeta administracion y dentro de ella tenemos el html de transporte
    return HttpResponse('Aca sale la lista de transportes');

def detalleTransporteView(request, id):
    return HttpResponse(f'Aca sale un transporte en detalle con id:{id}');

def registraTransporteView(request):
    nuevoTransporte = None
    if request.method == 'POST':
        transporteForm = TransporteForm(request.POST)
        if transporteForm.is_valid():
            nuevoTransporte = transporteForm.save(commit=False)
            nuevoTransporte.save()
            messages.success(
                request,
                'Se ha agregado correctamente el Punto Turistico {}'.format(nuevoTransporte))
            return redirect(reverse(
                '', args=(nuevoTransporte.id,)))

    else:
        transporteForm = TransporteForm()
    return HttpResponse('Aca se registran los transportes solamente'); #Aca vamos a hacer el render despue

def modificarTransporteView(request):
    return HttpResponse('Aca se modifica el transporte');

#Definicion de reportes

def reportesView(request):
    nuevoReporte = None
    if request.method == 'POST':
        reportesForm = ReportesForm(request.POST)
        if reportesForm.is_valid():
            nuevoReporte 

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
    nuevoPuntoTuristico = None
    if request.method == 'POST':
        formPuntoTuristico = PuntoTuristicoForm (request.POST, request.FILES)
        if formPuntoTuristico.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevoPuntoTuristico = formPuntoTuristico.save(commit=False)
            nuevoPuntoTuristico.save()
            # Guarda las relaciones ManyToMany (como el campo categorias)
            formPuntoTuristico.save_m2m()
            messages.success(
                request,
                'Se ha agregado correctamente el Punto Turistico {}'.format(nuevoPuntoTuristico))
            return redirect(reverse(
                '', args=(nuevoPuntoTuristico.id,)))
        
    else:
        formPuntoTuristico = PuntoTuristicoForm()

    return render(request, 'puntosTuristicos/formularioAgregarPuntoTuristico.html')



#Definicion de Recorridos;

def RecorridosView(request):
    return HttpResponse('Aca es la pagina de los Recorridos')

def listarRecorridos(request):
    return HttpResponse('Aca se mostrara una lista de los Recorridos')

def CrearRecorrido(request):
    return HttpResponse('Aqui se solicitara la informacion necesaria para crear un recorrido')

def modificarRecorridos(request):
    return HttpResponse('Aqui se mostrara la pagina de modificaciones')


#vistas de itinerarios

# Create your views here.
def crearItinerario (request):
    return HttpResponse ('aca sale la parte para crear un Itinerario')

def listarItinerarios (request):
    return HttpResponse('aca sale la lista de Itinerarios')

def modificarItinerarios (request):
    return HttpResponse ('aca esta la parte para modificar los Itinerarios')

def buscarItinerarioParticular (request, id):
    return HttpResponse(f'Aca sale un Itinerario particular con id:{id}')


#vistas de notificaciones
def crearNotificacion (request):
    return HttpResponse ('aca sale la parte para crear un Notificacion')

def listarNotificaciones (request):
    return HttpResponse('aca sale la lista de Notificaciones')

def modificarNotificacion (request):
    return HttpResponse ('aca esta la parte para modificar las Notificaciones')

def buscarNotificacionParticular (request, id):
    return HttpResponse(f'Aca sale un Notificacion particular con id:{id}')
