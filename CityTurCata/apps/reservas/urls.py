from django.urls import path
from apps.reservas.views import listarReservas, buscarResevaParticular, crearReserva, modificarReseva

app_name = 'reservas'
urlpatterns = [
    path('reservas/', listarReservas, name='listarReservas'),
    path('reservas/<int:id>', buscarResevaParticular,name= 'buscarResevaParticular'),
    path('reservas/crear', crearReserva,name= 'crearReserva'),
    path('reservas/modificar', modificarReseva,name= 'modificarReseva'),
]