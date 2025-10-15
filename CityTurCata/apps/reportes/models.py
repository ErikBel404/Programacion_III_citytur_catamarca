from django.db import models

# Create your models here.
class Reportes(models.Model):
    descripcionReportes = models.TextField(max_length=250, blank=False, null=False);
    tipoReportes = models.TextField(max_length=250, blank=False, null=False);

    def __str__(self):
        return f'Descripcion del reporte: {self.descripcionReportes}, tipo de reporte: {self.tipoReportes}'