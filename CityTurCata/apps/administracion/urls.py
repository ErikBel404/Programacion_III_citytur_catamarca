from django.urls import path
from apps.administracion.views import transporte_view

#app_name = 'transporte'

urlpatterns = [
    path('',transporte_view, name='listaTransporte')
]
