from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Persona(AbstractUser):
    dni = models.TextField(max_length=8, unique=True)

    def __str__(self):
        return f'DNI:{self.dni}'

class Administrador (Persona):
    domicilio = models.TextField(max_length=50, blank= False, null= False )
    categoria = models.TextField(max_length=20, blank= False, null= False )

    def __str__(self):
        return f'Domicilio:{self.domicilio} Categoria:{self.categoria}'

class Cliente(Persona):

    nombreInstitucion = models.TextField(max_length=100, blank= False, null= False )
    cuit= models.TextField(max_length=11, unique= True )

    def __str__(self):
        return f'Nombre Institucion: {self.nombreInstitucion} Cuit:{self.cuit}'

class Operario(Persona):
    domicilio = models.TextField(max_length=50, blank= False, null= False )
    categoria = models.TextField(max_length=20, blank= False, null= False )

    def __str__(self):
        return f'Domicilio:{self.domicilio} Categoria:{self.categoria}'
    
class Turista(Persona):
    nacionalidad= models.TextField(blank= False, null= False )
    def __str__(self):
        return f'Nacionalidad:{self.nacionalidad}'
    