from django import forms
from .models import PuntoTuristico
from apps.administracion.models import Transporte, Reportes, Recorrido, PuntoTuristico


class PuntoTuristicoForm (forms.ModelForm):
    class Meta:
        model = PuntoTuristico
        fields = [
            'nombre',
            'ubicacion',
            'informacion', 
            'imagen'
        ]
        widgets = {
        }



class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = ['dominioMatriculaTransporte',
                  'capacidadTransporte', 'estadoTransporte']

        widgets = {

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
        to_field_name='nombre',
        required=True,
        label='Seleccione el punto de inicio',
        empty_label="Seleccione..."
    )

    final = forms.ModelChoiceField(
        queryset=PuntoTuristico.objects.all(),
        to_field_name='nombre',
        required=True,
        label='Seleccione el punto final',
        empty_label="Seleccione..."
    )

    class Meta:
        model = Recorrido
        fields = ['nombreRecorrido', 'horarios',
                  'puntosTuristicos', 'inicio', 'final']

        widgets = {

        }

    def save(self, commit=True):
        recorrido = super().save(commit=False)
        recorrido.inicio = self.cleaned_data['inicio'].nombre
        recorrido.final = self.cleaned_data['final'].nombre
        if commit:
            recorrido.save()
            self.save_m2m()
        return recorrido