from django import forms
from .models import PuntoTuristico
from apps.administracion.models import Transporte, Reportes, Recorrido, PuntoTuristico, Notificacion


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
            'informacion': forms.TextInput(attrs={
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


class ReportesForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['tipoReportes', 'formatoReporte',
                  'horaFecha', 'identidadSolicitante']

        widgets = {

        }


class RecorridoForm(forms.ModelForm):
    inicio = forms.ModelChoiceField(
        queryset=PuntoTuristico.objects.all(),
        required=True,
        label='📌Punto partida:',
        empty_label=""
    )

    final = forms.ModelChoiceField(
        queryset=PuntoTuristico.objects.all(),
        required=True,
        label='📌Final recorrido:',
        empty_label=""
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
            'inicio': forms.Select(attrs={
                'class': 'inputLabel',
                'id': 'partidaNuevaPC', # ID de tu HTML estático
                'required': True
            }),
            'final': forms.Select(attrs={
                'class': 'inputLabel',
                'id': 'finalNuevoPc', # ID de tu HTML estático
                'required': True
            }),
            'horarios': forms.TimeInput(attrs={
                'type': 'time', # Para que sea un input de hora
                'class': 'inputLabel',
                'id': 'hora-recorrido',
                'required': True
            }),
            'puntosTuristicos': forms.CheckboxSelectMultiple(attrs={
                # Django pondrá los <li> y <label> automáticamente
                # No podemos agregar la clase 'checkboxItem' aquí
                # pero los pondremos dentro del acordeón
            }),
        }
        
        labels = {
            'nombreRecorrido':'🚌 Ingrese recorrido:', 
            'horarios': '🕑 Hora recorrido:',
            'puntosTuristicos': '📌Puntos turisticos:', 
        }

    def save(self, commit=True):
        recorrido = super().save(commit=False)
        recorrido.inicio = self.cleaned_data['inicio'].nombre
        recorrido.final = self.cleaned_data['final'].nombre
        if commit:
            recorrido.save()
            self.save_m2m()
        return recorrido
    


class NotificacionForm(forms.ModelForm):
    model =Notificacion
    fields = ['titulo', 'descripcion']

    widgets = {

    }