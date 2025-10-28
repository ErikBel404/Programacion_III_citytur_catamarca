from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def crearReserva (request):
    return HttpResponse ('aca sale la parte para crear una reserva')

def listarReservas (request):
    return HttpResponse('aca sale la lista de las reservas')

def modificarReseva (request):
    return HttpResponse ('aca esta la parte para modificar las reservas')

def buscarResevaParticular (request, id):
    return HttpResponse(f'Aca sale una reserva particular con id:{id}')

