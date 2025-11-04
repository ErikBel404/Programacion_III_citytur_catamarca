from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    documento_identidad = models.CharField(max_length=15, verbose_name='Número de documento', unique=True)
    domicilio = models.CharField(max_length=250)
    tipoUsuario = models.CharField (max_length=50, blank=False, null=False);
    

    def __str__(self):
        return f'{self.username}'

