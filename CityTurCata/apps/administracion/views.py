from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse

#importaciones de los modelos
from apps.administracion.models import PuntoTuristico, Transporte, Recorrido, Reportes, Itinerario, Notificacion

#importaciones de los form
from .forms import TransporteForm, ReportesForm, RecorridoForm, NotificacionForm, PuntoTuristicoForm, ItinerarioForm


#=========================================================Definicion de transporte de las vistas de transporte(lo separo asi por que me pierdo si no)=========================================================

def listaTransportesView(request):
    transportesVista = Transporte.objects.all()

    contexto = {
        'transportes' : transportesVista
    }

    return render(request, 'transporte/visualizarTransporte.html',contexto)



def registraTransporteView(request):
    nuevoTransporte = None
    if request.method == 'POST':
        transporteForm = TransporteForm(request.POST)
        if transporteForm.is_valid():
            nuevoTransporte = transporteForm.save(commit=False)
            nuevoTransporte.save()
            transporteForm.save_m2m()
            
            return redirect('administracion:listaTransporte')
           
    else:
        transporteForm = TransporteForm()

    contexto = {
        'transportes': transporteForm
    }

    return render(request,'transporte/formularioAgregarTransporte.html',contexto)



def modificarTransporteView(request,pk):
    TransporteViejo = get_object_or_404(Transporte, pk=pk)

    if request.method == 'POST':
        transporteNuevoForm = TransporteForm(request.POST, instance=TransporteViejo)
        if transporteNuevoForm.is_valid():
            transporteNuevoForm.save(commit = True)
            messages.success(request, 'Se ha actulizado correctamente el transporte{}'.format(transporteNuevoForm))

            return redirect('administracion:listaTransporte')
        
    else:
        transporteNuevoForm = TransporteForm(instance=TransporteViejo)

    contexto = {
        'transportes': transporteNuevoForm
    }

    return render(request,'transporte/formularioAgregarTransporte.html',contexto)



def bajaTransporteView(request,pk):
    bajaTransporte = get_object_or_404(Transporte, pk=pk)
    bajaTransporte.delete()

    return redirect('administracion:listaTransporte')


#=========================================================Definicion de transporte de las vistas de reportes(lo separo asi por que me pierdo si no)=========================================================

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



#=========================================================Definicion de transporte de las vistas de puntos Turisticos(lo separo asi por que me pierdo si no)=========================================================
def listarPuntosTuristicosView(request):
    puntosTuristicosVista = PuntoTuristico.objects.all();

    contexto = {
        'puntos' : puntosTuristicosVista
    }

    return render(request, 'puntosTuristicos/visualizarPuntoTuristico.html',contexto)



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

            return redirect('administracion:listaPuntosTuristicos')
   
    else:
        formPuntoTuristico = PuntoTuristicoForm()
        
    contexto = {
        'form': formPuntoTuristico
    }
    return render(request, 'puntosTuristicos/formularioAgregarPuntoTuristico.html', contexto )




def modificarPuntoTuristicosView(request, pk):

    puntoViejo= get_object_or_404(PuntoTuristico, pk=pk)

    if request.method == 'POST':
        puntoNuevoForm = PuntoTuristicoForm(
            request.POST, request.FILES, instance=puntoViejo)
        if puntoNuevoForm.is_valid():
            puntoNuevoForm.save(commit=True)
            messages.success(request,
                           'Se ha actualizado correctamente el Punto Turistico {}'.format(puntoNuevoForm) )
            
            return redirect('administracion:listaPuntosTuristicos')
    else:
        puntoNuevoForm = PuntoTuristicoForm(instance=puntoViejo)

    contexto = {
        'form': puntoNuevoForm
    }
    return render(request,
                  'puntosTuristicos/formularioAgregarPuntoTuristico.html', contexto)

    

def bajaPuntoTuristicosView(request,pk):
    bajaPunto = get_object_or_404(PuntoTuristico, pk = pk)
    bajaPunto.delete()
    
    return redirect('administracion:listaPuntosTuristicos')



#=========================================================Definicion de transporte de las vistas de Recorridos(lo separo asi por que me pierdo si no)=========================================================

def listarRecorridosView(request):
    recorridoView = Recorrido.objects.all();

    contexto = {
        'recorridos' : recorridoView
    }

    return render(request,'recorrido/visualizarRecorridos.html',contexto)



def crearRecorridosView(request):
    nuevoRecorrido = None
    recorridoForm = RecorridoForm(request.POST)
    if recorridoForm.is_valid():
        nuevoRecorrido = recorridoForm.save(commit=False)
        nuevoRecorrido.save()

        recorridoForm.save_m2m()

        return redirect('administracion:ListarRecorridos')

    else:
        recorridoForm = RecorridoForm()

    contexto = {
        'form' : recorridoForm
    }

    return render(request, 'recorrido/agregarRecorrido.html', contexto)


def modificarRecorridosView(request, pk):

    recorridoViejo= get_object_or_404(Recorrido, pk=pk)

    if request.method == 'POST':
        recorridoNuevoForm = RecorridoForm(
            request.POST, request.FILES, instance=recorridoViejo)
        if recorridoNuevoForm.is_valid():
            recorridoNuevoForm.save(commit=True)
            messages.success(request,
                           'Se ha actualizado correctamente el Punto Turistico {}'.format(recorridoNuevoForm) )
            
            return redirect('administracion:ListarRecorridos')
    else:
        recorridoNuevoForm = RecorridoForm(instance=recorridoViejo)

    contexto = {
        'form': recorridoNuevoForm
    }
    return render(request,
                  'recorrido/agregarRecorrido.html', contexto)




def bajaRecorridosView(request,pk):
    bajaRecorrido = get_object_or_404(Recorrido, pk = pk)
    bajaRecorrido.delete()
    
    return redirect('administracion:ListarRecorridos')



#=========================================================Definicion de transporte de las vistas de Itinerarios(lo separo asi por que me pierdo si no)=========================================================

def listarItinerariosView(request):
    itinerarioView = Itinerario.objects.all().order_by('-fecha') # Ordenamos por fecha

    contexto = {
        'itinerarios': itinerarioView 
    }
    return render(request, 'itinerario/visualizarItinerarios.html', contexto)


def crearItinerarioView(request):
    # Usando tu lógica de 'crearRecorridosView'
    if request.method == 'POST':
        itinerarioForm = ItinerarioForm(request.POST)
        if itinerarioForm.is_valid():
            itinerarioForm.save() 
            messages.success(request, '¡Itinerario creado exitosamente!')
            return redirect('administracion:listarItinerarios') 
    else:
        itinerarioForm = ItinerarioForm()

    contexto = {
        'form': itinerarioForm
    }
    return render(request, 'itinerario/formularioAgregarItinerario.html', contexto)


def modificarItinerarioView(request, pk):
    itinerarioViejo = get_object_or_404(Itinerario, pk=pk)

    if request.method == 'POST':
        itinerarioNuevoForm = ItinerarioForm(request.POST, instance=itinerarioViejo)
        if itinerarioNuevoForm.is_valid():
            itinerarioNuevoForm.save()
            messages.success(request, 'Se ha actualizado correctamente el Itinerario')
            return redirect('administracion:ListarItinerarios') 
    else:
        itinerarioNuevoForm = ItinerarioForm(instance=itinerarioViejo)

    contexto = {
        'form': itinerarioNuevoForm
    }
    return render(request, 'itinerario/formularioAgregarItinerario.html', contexto)


def bajaItinerarioView(request, pk):
    bajaItinerario = get_object_or_404(Itinerario, pk=pk)
    bajaItinerario.delete()
    
    messages.success(request, 'Itinerario eliminado.')
    return redirect('administracion:listarItinerarios')

    
#=========================================================Definicion de transporte de las vistas de Notificacion(lo separo asi por que me pierdo si no)=========================================================
def listarNotificacionesView (request):
    notificacionView = Notificacion.objects.all()

    contexto  = {
        'notificaciones' : notificacionView 
    }

    return render(request,'notificaciones/visualizarNotificaciones.html',contexto)



def crearNotificacionView (request):
    nuevoNotificacion = None
    if request.method == 'POST':
        notificacionForm = NotificacionForm(request.POST)
        if notificacionForm.is_valid():
            nuevoNotificacion = notificacionForm.save(commit=False)
            nuevoNotificacion.save()

            notificacionForm.save_m2m()
            
            return redirect('administracion:listarNotificaciones')
    else:
        notificacionForm = NotificacionForm()
    
    contexto = {
        'notificaciones':notificacionForm
    }

    return render(request,'notificaciones/formularioAgregarNotificacion.html',contexto)
        

def modificarNotificacionView (request,pk):
    notificacionVieja = get_object_or_404(Notificacion, pk=pk)

    if request.method == 'POST':
        notificacionNuevaForm = NotificacionForm(request.POST, instance=notificacionVieja)
        if notificacionNuevaForm.is_valid():
            notificacionNuevaForm.save(commit=True)

            return redirect('administracion:listarNotificaciones')
    else:
        notificacionNuevaForm = NotificacionForm(instance=notificacionVieja)

    contexto = {
        'notificaciones':notificacionNuevaForm
    }

    return render(request,'notificaciones/formularioAgregarNotificacion.html',contexto)



def bajaNotificacionView(request,pk):
    bajaNotificacion = get_object_or_404(Notificacion, pk=pk)
    bajaNotificacion.delete()

    return redirect('administracion:listarNotificaciones')

def index_view(request):
    return render(request, 'index.html')