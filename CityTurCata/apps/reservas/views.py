from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apps.administracion.models import Itinerario
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.urls import reverse

from apps.reservas.models import Reserva
from .forms import ReservaForm

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
            itinerario_obj, creado = Itinerario.objects.get_or_create(fecha=fechaSeleccionada)

            if creado:
                itinerario_obj.titulo = f"Itinerario para {fechaSeleccionada.strftime('%d-%m-%Y')}"
                itinerario_obj.save()

            nuevaReserva = reservaForm.save(commit=False)
            nuevaReserva.save()
            reservaForm.save_m2m()

            return redirect('reservas:listarReservas')

    else:
        reservaForm = ReservaForm()

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
            reservaModificada.itinerario = itinerario_obj # Re-asigna el itinerario
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