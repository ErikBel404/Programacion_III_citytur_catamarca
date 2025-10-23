from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

##importaciones de los modelos
from apps.administracion.models import PuntoTuristico, Transporte, Recorrido, Reportes

#importaciones de los form
from .forms import TransporteForm, ReportesForm, RecorridoForm, NotificacionForm,PuntoTuristicoForm

# Create your views here.

#Definicion de transporte
def listaTransportesView(request):
    transportesVista = Transporte.objects.all()

    contexto = {
        'transportes' : transportesVista
    }

    return render(request, '',contexto)

def registraTransporteView(request):
    nuevoTransporte = None
    if request.method == 'POST':
        transporteForm = TransporteForm(request.POST)
        if transporteForm.is_valid():
            nuevoTransporte = transporteForm.save(commit=False)
            nuevoTransporte.save()
            transporteForm.save_m2m()

            messages.success(request, 'Se ha agregado correctamente el Punto Turistico {}'.format(nuevoTransporte))
            #return #redirect(reverse(
                #'', args=(nuevoTransporte.id,))
    else:
        transporteForm = TransporteForm()

    contexto = {
        'form': nuevoTransporte
    }

    return render(request,'',contexto)

def modificarTransporteView(request):
    return HttpResponse('Aca se modifica el transporte');

def bajaTransporteView(request):
    return HttpResponse('Aca se da de baja el transporte');


#Definicion de reportes

def reportesView(request):
    nuevoReporte = None
    if request.method == 'POST':
        reportesForm = ReportesForm(request.POST)
        if reportesForm.is_valid():
            nuevoReporte = reportesForm.save(commit=False)
            nuevoReporte.save()

            reportesForm.save_m2m()
            messages.success(request, 'Se ha creado correctamente el reporte: {}'.format(nuevoReporte))
    else:
        reportesForm = ReportesForm()

    contexto = {
        'form' : reportesForm
    }

    return render(request,'',contexto)

def listaReportesView(request):
    reportesView = Reportes.objects.all()

    contexto = {
        'reportes' : reportesView
    }

    return render(request,'',contexto)

def reporteRecorridosActivosView(request):
    return HttpResponse('Aca va el reporte de recorridos activos');

def reporteParadasMasUtilizadasView(request):
    return HttpResponse('Aca van el reporte de las paradas mas utilizadas');

def reporteReservasRecorridoView(resquest):
    return HttpResponse('Aca va el reporte de las reservas de los recorridos');

def reporteConsultaReservasView(request):
    return HttpResponse('Aca va el reporte de las consultas de las reservas');

def reporteEstadistaPasajerosView(request):
    return HttpResponse('Aca va el reporte de estadisticas en un rango de fechas')

#Definicion de puntos Turisticos;

def listarPuntosTuristicosView(request):
    puntosTuristicosVista = PuntoTuristico.objects.all();

    contexto = {
        'puntos' : puntosTuristicosVista
    }

    render(request, '',contexto)

def crearPuntosTuristicosView(request):
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
                'Se ha agregado correctamente el Punto Turistico: {}'.format(nuevoPuntoTuristico))
    
            #return redirect(reverse(
            #   '../', args=(nuevoPuntoTuristico.id,)))    
    else:
        formPuntoTuristico = PuntoTuristicoForm()
        
    contexto = {
        'form': formPuntoTuristico
    }
    return render(request, 'puntosTuristicos/formularioAgregarPuntoTuristico.html', contexto )

def modificarPuntoTuristicosView(request):
    return HttpResponse('Aca es la pagina de los Recorridos')


def bajaPuntoTuristicosView(request):
    return HttpResponse('Aca es la pagina de los Recorridos')


#Definicion de Recorridos;

def listarRecorridosView(request):
    recorridoView = Recorrido.objects.all();

    contexto = {
        'recorridos' : recorridoView
    }

    return render(request,'',contexto)

def crearRecorridosView(request):
    nuevoRecorrido = None
    recorridoForm = RecorridoForm(request.POST)
    if recorridoForm.is_valid():
        nuevoRecorrido = recorridoForm.save(commit=False)
        nuevoRecorrido.save()

        recorridoForm.save_m2m()

        messages.success(request, 'Se ha agrega correctamente el Recorrido: {}'.format(nuevoRecorrido))

    else:
        recorridoForm = RecorridoForm()

    contexto = {
        'form' : recorridoForm
    }

    return render(request,'', contexto)

    
def modificarRecorridosView(request):
    return HttpResponse('Aqui se mostrara la pagina de modificaciones')

def bajaRecorridosView(request):
    return HttpResponse('Aqui se mostrara la pagina de modificaciones')


#vistas de itinerarios -- hasta aca toqe yo no tocar mas  haya de aca belicho
def crearItinerarios (request):
    return HttpResponse ('aca sale la parte para crear un Itinerario')

def listarItinerarios (request):
    return HttpResponse('aca sale la lista de Itinerarios')

def modificarItinerarios (request):
    return HttpResponse ('aca esta la parte para modificar los Itinerarios')

def bajaItinerarios (request):
    return HttpResponse ('aca esta la parte para modificar los Itinerarios')

#vistas de notificaciones
def crearNotificacion (request):
    nuevoNotificacion = None
    if request.method == 'POST':
        notificacionForm = NotificacionForm(request.POST)
        if notificacionForm.is_valid():
            nuevoNotificacion = notificacionForm.save(commit=False)
            nuevoNotificacion.save()

            notificacionForm.save_m2m()
            messages.success(
                request, 'Se agrego la notificacion de manera correcta: {}'.format(nuevoNotificacion))
    else:
        notificacionForm = NotificacionForm()
    
    contexto = {
        'form':notificacionForm
    }

    return render(request,'',contexto)
        
def listarNotificaciones (request):
    return HttpResponse('aca sale la lista de Notificaciones')

def modificarNotificacion (request):
    return HttpResponse ('aca esta la parte para modificar las Notificaciones')

def buscarNotificacionParticular (request, id):
    return HttpResponse(f'Aca sale un Notificacion particular con id:{id}')
