from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
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

    return render(request,'',contexto)


def crearReservaView(request):
    nuevaReserva = None
    if request.method == 'POST':
        reservaForm = ReservaForm(request.POST)
        if reservaForm.is_valid():
            nuevaReserva = reservaForm.save(commit=False)
            nuevaReserva.save()
            reservaForm.save_m2m()

            return redirect('reservas:listarReservas')

    else:
        reservaForm = ReservaForm()

    contexto = {
        'reservas' : reservaForm
    } 

    return render(request,'',contexto)


def modificarReservaView (request,pk):
    reservaVieja = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        reservaNuevaForm = ReservaForm(request.POST, instance=reservaVieja)
        if reservaNuevaForm.is_valid():
            reservaNuevaForm.save(commit = True)
            messages.success(request,'Se ha actulizado correctamente la reserva{}'.format(reservaNuevaForm))

            return redirect('reservas:listarReservas')
    else:
        reservaNuevaForm = ReservaForm(instance=reservaVieja)

    contexto = {
        'reservas' : reservaNuevaForm
    }            

    return render(request,'',contexto)


def bajaReservaView (request, pk):
    bajaReserva = get_object_or_404(Reserva, pk=pk)
    bajaReserva.delete()

    return render('reservas:listarReservas')