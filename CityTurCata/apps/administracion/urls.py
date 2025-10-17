from django.urls import path
from apps.administracion.views import lista_transportes_view,detalle_transporte_view

app_name = 'administracion'

urlpatterns = [
    path('transportes/',lista_transportes_view, name='listaTransporte'),
    path('transportes/<int:id>/',detalle_transporte_view, name='detalleTransporte')
]
