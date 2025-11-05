from django import forms
from .models import PuntoTuristico
from apps.administracion.models import Transporte, Recorrido, PuntoTuristico, Notificacion, Itinerario


class PuntoTuristicoForm (forms.ModelForm):
    def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            if self.instance and self.instance.pk:
                self.fields['imagen'].required = False
            
    class Meta:
        model = PuntoTuristico
        fields = [
            'nombre',
            'ubicacion',
            'informacion', 
            'imagen'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'inputLabel',
                'id': 'nombre-puntoTuristico',
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'inputLabel',
                'id': 'ubicacion',
            }),
            'informacion': forms.Textarea(attrs={
                'class': 'inputLabel',
                'id': 'informacionPuntoTuristico',
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'inputArchivoOculto',
                'id': 'imgPuntoTuristico',
            }),
        }

        labels = {
            'nombre': '🚩 Nombre:',
            'ubicacion': '📌 Ubicacion:',
            'informacion': '📰 Informacion:',
            'imagen': '🏞️  Imagen:',
        }
        


class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = ['dominioMatriculaTransporte',
                  'capacidadTransporte', 'estadoTransporte']

        widgets = {
            'dominioMatriculaTransporte': forms.TextInput(attrs={
                'class': 'inputLabel',
                'id' :'dominioTransporte'
                }),

            'capacidadTransporte': forms.NumberInput(attrs={
                'class': 'inputLabel',
                'id' :'capacidadTransporte'
                }),

            'estadoTransporte':forms.Select(attrs={
                'class': 'inputLabel',
                'id' :'estadoTransporte'
                })
        }

        labels = {
            'dominioMatriculaTransporte':'🚍 Dominio:',
            'capacidadTransporte':'💺 Cantidad Asientos:',
            'estadoTransporte':'📢Estado Transporte:'
        }

class ReporteForm(forms.Form):
    
    TIPOINFORME = [
        ('', ''), 
        ('recorridos_activos', 'Recorridos Activos'),
        ('paradas_utilizadas', 'Paradas Más Utilizadas'),
        ('reservaRecorrido', 'Listado de Reservas por Recorrido'), 
        ('consultasReservas', 'Consulta de Reservas (Turista)'), 
        ('estadisticasPasajeros', 'Estadísticas de Pasajeros'), 
    ]

    FORMATODOCUMENTO = [
        ('csv', 'CSV'),
        ('excel', 'Excel (.xlsx)'),
        ('pdf', 'PDF'),
    ]

    tipoReportes = forms.ChoiceField(
        choices=TIPOINFORME,
        label="📋 Tipo de Reporte",
        widget=forms.Select(attrs={'class': 'inputLabel', 'id': 'id_tipo_reporte'})
    )
    
    formatoReporte = forms.ChoiceField(
        choices=FORMATODOCUMENTO,
        label="🗂️ Formato de Archivo",
        widget=forms.Select(attrs={'class': 'inputLabel', 'id': 'id_formato_reporte'})
    )
        
    
    recorrido = forms.ModelChoiceField(
        queryset=Recorrido.objects.all(), 
        required=False,
        label="Seleccione un Recorrido",
        widget=forms.Select(attrs={'class': 'inputLabel', 'id': 'id_recorrido'})
    )

    fecha_inicio = forms.DateField(
        required=False,
        label="Fecha Desde",
        widget=forms.DateInput(attrs={'class': 'inputLabel', 'type': 'date', 'id': 'id_fecha_inicio'})
    )
    
    fecha_fin = forms.DateField(
        required=False,
        label="Fecha Hasta",
        widget=forms.DateInput(attrs={'class': 'inputLabel', 'type': 'date', 'id': 'id_fecha_fin'})
    )


class RecorridoForm(forms.ModelForm):
    
    inicio = forms.ModelChoiceField(
        queryset=PuntoTuristico.objects.all(),
        required=True,
        label='📌Punto partida:',
        empty_label="",
        widget=forms.Select(attrs={
            'class': 'inputLabel',
            'id': 'partidaNuevaPC', 
            'required': True
        })
    )

    final = forms.ModelChoiceField(
        queryset=PuntoTuristico.objects.all(),
        required=True,
        label='📌Final recorrido:',
        empty_label="",
        widget=forms.Select(attrs={
            'class': 'inputLabel',
            'id': 'finalNuevoPc', 
            'required': True
        })
    )


    class Meta:
        model = Recorrido
        fields = ['nombreRecorrido', 'horarios',
                  'puntosTuristicos', 'inicio', 'final']

        widgets = {
            
            'nombreRecorrido': forms.TextInput(attrs={
                'class': 'inputLabel',
                'id': 'nombre-recorrido',
                'maxlength': 70,
                'required': True
            }),
            'horarios': forms.TimeInput(attrs={
                'type': 'time', 
                'class': 'inputLabel',
                'id': 'hora-recorrido',
                'required': True
            }),
            'puntosTuristicos': forms.CheckboxSelectMultiple(attrs={
               
            }),
        }
        
        labels = {
            'nombreRecorrido':'🚌 Ingrese recorrido:', 
            'horarios': '🕑 Hora recorrido:',
            'puntosTuristicos': '📌Puntos turisticos:', 
        }



class NotificacionForm(forms.ModelForm):
    class Meta:
        model =Notificacion
        fields = ['titulo', 'descripcion', 'administrador', 'operario', 'itinerario']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class' : 'inputLabel',
                'id': 'tituloNotificacion'}),

            'descripcion': forms.Textarea(attrs={
                'class' : 'inputLabel',
                'id': 'descripcionNotificacion'}),
        }

        labels = {
            'titulo':'📎Titulo',
            'descripcion': '📄Descripcion De la Notificacion'
        }


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = [
            'fecha',
            'titulo',
            'transporte',
            'recorridos',
            
        ]
        
        widgets = {
            'fecha': forms.DateInput(attrs={
                'class': 'inputLabel',
                'type': 'date'
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'inputLabel',
                'id': 'tituloItinerario'
            }),
            'transporte': forms.Select(attrs={
                'class': 'inputLabel',
                'id': 'transporteItinerario'
            }),
            'recorridos': forms.Select(attrs={
                'class': 'inputLabel',
                'id': 'recorridoItinerario'
            })
        }

        labels = {
            'fecha': '📅 Fecha del Itinerario',
            'titulo': '🏷️ Título (Opcional)',
            'transporte': '🚌 Transporte Asignado',
            'recorridos': '🛣️ Recorrido Principal',
        }