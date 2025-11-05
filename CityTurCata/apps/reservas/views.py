from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apps.administracion.models import Itinerario,Transporte
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.urls import reverse

from apps.reservas.models import Reserva
from .forms import ReservaForm

from .models import Recorrido # Asegúrate de importar todos los modelos
from django.db.models import Sum # <-- ¡NUEVA IMPORTACIÓN!


# Create your views here.

def listarReservasView (request):
    reservaVista = Reserva.objects.all()

    contexto = {
        'reservas' : reservaVista
    }

    return render(request,'reserva/visualizarReservas.html',contexto)




@login_required
def crearReservaView(request):
    nuevaReserva = None
    if request.method == 'POST':
        reservaForm = ReservaForm(request.POST)
        if reservaForm.is_valid():

            fechaSeleccionada = reservaForm.cleaned_data['fechaReserva']
            recorridoSeleccionado = reservaForm.cleaned_data['recorridoReserva']

            try:
                # Intenta encontrar el itinerario exacto (fecha + recorrido)
                itinerario_obj = Itinerario.objects.get(
                    fecha=fechaSeleccionada,
                    recorridos=recorridoSeleccionado
                )
            
            
            # --- ESTE BLOQUE 'EXCEPT' ES EL QUE MODIFICAMOS ---
            except Itinerario.DoesNotExist:
                
                print("\n---  DEBUG DE TRANSPORTE INICIADO ---")
                print(f"DEBUG: Fecha seleccionada: {fechaSeleccionada}")

                # 1. Obtener los IDs de transportes YA OCUPADOS en esa fecha
                transportes_ocupados_ids_query = Itinerario.objects.filter(
                    fecha=fechaSeleccionada
                ).values_list('transporte__id', flat=True)
                
                # Forzamos la consulta para verla en el print
                transportes_ocupados_ids = list(transportes_ocupados_ids_query) 
                print(f"DEBUG: IDs de transportes YA OCUPADOS: {transportes_ocupados_ids}")
                
                # 2. Buscar un transporte que cumpla AMBAS condiciones:
                transporte_disponible = Transporte.objects.filter(
                    estadoTransporte='activo'  # <-- Solo buscar transportes ACTIVOS
                ).exclude(
                    id__in=transportes_ocupados_ids
                ).first()
                
                # ESTE ES EL PRINT MÁS IMPORTANTE
                print(f"DEBUG: Transporte disponible ENCONTRADO: {transporte_disponible}")
                print("--- DEBUG DE TRANSPORTE FINALIZADO ---\n")
                
                # 3. Si .first() no encontró nada, transporte_disponible será None
                if not transporte_disponible:
                    # El mensaje de error ahora es más preciso
                    reservaForm.add_error(None, 'No hay transportes activos disponibles para crear un nuevo itinerario en esta fecha (todos están en uso).')
                    contexto = {'reservas': reservaForm} 
                    return render(request, 'reserva/formularioAgregarReserva.html', contexto)

                # 4. Si encontramos un transporte, creamos el nuevo itinerario con él
                itinerario_obj = Itinerario.objects.create(
                    fecha=fechaSeleccionada,
                    recorridos=recorridoSeleccionado,
                    transporte=transporte_disponible,
                    titulo=f"Itinerario para {recorridoSeleccionado.nombreRecorrido} - {fechaSeleccionada.strftime('%d-%m-%Y')}"
                )
            
            # --- EL RESTO DE LA VISTA SIGUE IGUAL ---
   
            asientos_solicitados = reservaForm.cleaned_data['cantidadReserva']

            if asientos_solicitados <= 0:
                reservaForm.add_error('cantidadReserva', 'La cantidad de asientos debe ser al menos 1.')
                contexto = {'reservas': reservaForm} 
                return render(request, 'reserva/formularioAgregarReserva.html', contexto)

            capacidad_total = itinerario_obj.transporte.capacidadTransporte
            
            reservas_activas = Reserva.objects.filter(
                itinerario=itinerario_obj,
                estadoReserva='reservaActiva' # Solo contamos las activas
            )
            
            datos_agregados = reservas_activas.aggregate(
                total_ocupados=Sum('cantidadReserva')
            )
            
            asientos_ocupados = datos_agregados['total_ocupados'] or 0
            
            asientos_disponibles = capacidad_total - asientos_ocupados
            
            if asientos_solicitados > asientos_disponibles:
                error_msg = f"No hay suficientes asientos disponibles. Solo quedan {asientos_disponibles}."
                if asientos_disponibles <= 0:
                    error_msg = "Lo sentimos, este itinerario ya está completo."
                
                reservaForm.add_error('cantidadReserva', error_msg)
                
                contexto = {'reservas': reservaForm} 
                return render(request, 'reserva/formularioAgregarReserva.html', contexto)

            nuevaReserva = reservaForm.save(commit=False)
            nuevaReserva.itinerario = itinerario_obj
            nuevaReserva.turista = request.user
            nuevaReserva.estadoReserva = 'reservaActiva' 
            nuevaReserva.save()
                
            return redirect('reservas:listarReservas')

    else:
        recorrido_id = request.GET.get('recorrido_id')
        initial_data = {}
        
        if recorrido_id:
            try:
                # Usamos el ID de la URL para obtener el objeto Recorrido
                # (Recorrido debe estar importado: from .models import Recorrido)
                recorrido_obj = get_object_or_404(Recorrido, id=recorrido_id)
                
                # 2. Pre-llenamos el campo con el objeto
                # 'recorridoReserva' debe ser el nombre del campo en tu ReservaForm
                initial_data['recorridoReserva'] = recorrido_obj
                
            except Exception:
                # Si el ID en la URL es incorrecto, el formulario se carga sin pre-llenar.
                pass
        
        # 3. Inicializamos el formulario, aplicando los datos iniciales si existen
        # Si initial_data está vacío, se crea un formulario en blanco, como antes.
        reservaForm = ReservaForm(initial=initial_data)

    contexto = {
        'reservas' : reservaForm
        } 
    return render(request,'reserva/formularioAgregarReserva.html',contexto)


def modificarReservaView (request,pk):
    reservaVieja = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        reservaNuevaForm = ReservaForm(request.POST, instance=reservaVieja)
        if reservaNuevaForm.is_valid():

            fechaSeleccionada = reservaNuevaForm.cleaned_data['fechaReserva']
            itinerario_obj, creado = Itinerario.objects.get_or_create(fecha=fechaSeleccionada)
            if creado:
                itinerario_obj.titulo = f"Itinerario para {fechaSeleccionada.strftime('%d-%m-%Y')}"
                itinerario_obj.save()

            reservaModificada = reservaNuevaForm.save(commit=False)
            reservaModificada.itinerario = itinerario_obj
            reservaModificada.save()            

            messages.success(request,'Se ha actulizado correctamente la reserva{}'.format(reservaModificada))

            return redirect('reservas:listarReservas')
    else:
        reservaNuevaForm = ReservaForm(instance=reservaVieja)

    contexto = {
        'reservas' : reservaNuevaForm
    }            

    return render(request,'reserva/formularioAgregarReserva.html',contexto)


def bajaReservaView (request, pk):
    bajaReserva = get_object_or_404(Reserva, pk=pk)
    bajaReserva.delete()

    return redirect('reservas:listarReservas')







