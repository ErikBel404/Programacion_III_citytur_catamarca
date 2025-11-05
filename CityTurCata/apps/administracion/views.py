from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse

#para los reportes no tocar(de lala para belicho)
from django.http import HttpResponse
from .utils import generar_csv, generar_excel, generar_pdf 

#importaciones de los modelos
from apps.administracion.models import PuntoTuristico, Transporte, Recorrido, Itinerario, Notificacion
from apps.reservas.models import Reserva
from django.db.models import Count,Sum

#importaciones de los form
from .forms import TransporteForm, ReporteForm, RecorridoForm, NotificacionForm, PuntoTuristicoForm, ItinerarioForm


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
    form = ReporteForm()
    contexto = {
        'form': form
    }
    return render(request, 'reportes/panelReportes.html', contexto)


# Recorridos Activos
def reporteRecorridosActivosView(request):
    formato = request.GET.get('formato', 'pdf')
    recorridos = Recorrido.objects.filter(activo=True) 

    titulo = "Recorridos_Activos"
    cabecera = ['ID', 'Título', 'Duración', 'Descripción']
    datos = []
    for r in recorridos:
       
        datos.append([r.id, r.titulo, r.duracion, r.descripcion]) 

    if formato == 'csv':
        return generar_csv(titulo, cabecera, datos)
    elif formato == 'excel':
        return generar_excel(titulo, cabecera, datos)
    elif formato == 'pdf':
        return generar_pdf(titulo, "Reporte de Recorridos Activos", cabecera, datos)
    
    return HttpResponse("Formato no válido.")

# Paradas Más Utilizadas
def reporteParadasMasUtilizadasView(request):
    formato = request.GET.get('formato', 'pdf')

   
    paradas = PuntoTuristico.objects.annotate(
        num_reservas=Count('puntosDePartida') 
    ).filter(num_reservas__gt=0).order_by('-num_reservas')

    titulo = "Paradas_Mas_Utilizadas"
    cabecera = ['Nombre de Parada', 'Cantidad de Usos']
    datos = []
    for p in paradas:
        datos.append([p.nombre, p.num_reservas])

    if formato == 'csv':
        return generar_csv(titulo, cabecera, datos)
    elif formato == 'excel':
        return generar_excel(titulo, cabecera, datos)
    elif formato == 'pdf':
        return generar_pdf(titulo, "Reporte de Paradas Más Utilizadas", cabecera, datos)

    return HttpResponse("Formato no válido.")

#Reportes de reservas por recorrido
def reporteReservasRecorridoView(request):
    formato = request.GET.get('formato', 'pdf')
    recorrido_id = request.GET.get('recorrido_id')

    if not recorrido_id:
        messages.error(request, "Debe seleccionar un recorrido para este reporte.")
        return HttpResponse("Error: No se especificó un recorrido.")
        
    recorrido = get_object_or_404(Recorrido, pk=recorrido_id)
    
    reservas = Reserva.objects.filter(recorridoReserva=recorrido).order_by('fechaReserva')

    titulo = f"Reservas_del_{recorrido.titulo}"
    titulo_pdf = f"Reservas del Recorrido: {recorrido.titulo}"
    cabecera = ['ID Reserva', 'Turista', 'Fecha', 'Hora', 'Cantidad', 'Estado']
    datos = []
    for r in reservas:
        datos.append([
            r.id,
            str(r.turista), 
            r.fechaReserva.strftime('%d/%m/%Y'),
            r.horaReserva.strftime('%H:%M'),
            r.cantidadReserva,
            r.get_estadoReserva_display() 
        ])

    if formato == 'csv':
        return generar_csv(titulo, cabecera, datos)
    elif formato == 'excel':
        return generar_excel(titulo, cabecera, datos)
    elif formato == 'pdf':
        return generar_pdf(titulo, titulo_pdf, cabecera, datos)

    return HttpResponse("Formato no válido.")


# Reporte de consulta de reservas
def reporteConsultaReservasView(request):
    formato = request.GET.get('formato', 'pdf')
    
    reservas = Reserva.objects.all().select_related(
        'turista', 'recorridoReserva'
    ).order_by('turista__username', 'fechaReserva')

    titulo = "Consulta_General_Reservas"
    titulo_pdf = "Consulta General de Reservas"
    cabecera = ['Turista', 'Recorrido', 'Fecha', 'Hora', 'Cantidad', 'Estado']
    datos = []
    for r in reservas:
        datos.append([
            str(r.turista),
            str(r.recorridoReserva),
            r.fechaReserva.strftime('%d/%m/%Y'),
            r.horaReserva.strftime('%H:%M'),
            r.cantidadReserva,
            r.get_estadoReserva_display()
        ])

    if formato == 'csv':
        return generar_csv(titulo, cabecera, datos)
    elif formato == 'excel':
        return generar_excel(titulo, cabecera, datos)
    elif formato == 'pdf':
        return generar_pdf(titulo, titulo_pdf, cabecera, datos)

    return HttpResponse("Formato no válido.")


#Reporte de estadisticas de pasajeros
def reporteEstadistaPasajerosView(request):
    formato = request.GET.get('formato', 'pdf')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if not (fecha_inicio and fecha_fin):
        messages.error(request, "Debe seleccionar un rango de fechas (Desde y Hasta).")
        return HttpResponse("Error: No se especificó un rango de fechas.")

    stats = Reserva.objects.filter(
        fechaReserva__range=[fecha_inicio, fecha_fin]
    ).values(
        'recorridoReserva__titulo' 
    ).annotate(
        total_pasajeros=Sum('cantidadReserva') 
    ).order_by('-total_pasajeros') 

    titulo = f"Estadisticas_Pasajeros_{fecha_inicio}_al_{fecha_fin}"
    titulo_pdf = f"Estadísticas de Pasajeros ({fecha_inicio} al {fecha_fin})"
    cabecera = ['Recorrido', 'Total Pasajeros']
    datos = []
    for s in stats:
        datos.append([
            s['recorridoReserva__titulo'], 
            s['total_pasajeros']
        ])

    if formato == 'csv':
        return generar_csv(titulo, cabecera, datos)
    elif formato == 'excel':
        return generar_excel(titulo, cabecera, datos)
    elif formato == 'pdf':
        return generar_pdf(titulo, titulo_pdf, cabecera, datos)

    return HttpResponse("Formato no válido.")

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
            nuevoPuntoTuristico = formPuntoTuristico.save(commit=False)
            nuevoPuntoTuristico.save()
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


def crearItinerariosView(request):
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


def modificarItinerariosView(request, pk):
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


def bajaItinerariosView(request, pk):
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