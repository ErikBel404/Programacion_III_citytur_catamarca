from django.shortcuts import render
from django.http import HttpResponse

from apps.administracion.models import Transporte

# Create your views here.

#Definicion de transporte
def transporte_view(request):
    #return render(request, 'administracion/transporte.html')   -> suponiendo que creamos una carpetea template dentro de la misma ponemos una carpeta administracion y dentro de ella tenemos el html de transporte

    return HttpResponse('ACA VA TRANSPORTE GIL')



#Definicion