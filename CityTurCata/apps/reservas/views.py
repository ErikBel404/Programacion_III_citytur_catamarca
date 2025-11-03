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


def modificarResevaView (request,pk):


    
    return HttpResponse ('aca esta la parte para modificar las reservas')

def bajaReservaView (request, pk):
    return HttpResponse(f'Aca sale una reserva particular con id:{id}')

