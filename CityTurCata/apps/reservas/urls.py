from django.urls import path
from apps.reservas import views

app_name = 'reservas'

urlpatterns = [
    path('reservas/lista/', views.listarReservasView, name='listarReservas'),
    path('reservas/agregar/',views.crearReservaView, name='agregarReserva'),
    path('reservas/modificar/<int:pk>/', views.modificarReservaView, name='modificarReseva'),
    path('reservas/baja/<int:pk>', views.bajaReservaView, name='bajaReserva')
]