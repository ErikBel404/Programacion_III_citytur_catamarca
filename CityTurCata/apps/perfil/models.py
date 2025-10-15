from django.db import models

# Create your models here.
class Persona(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    correo = models.TextField(max_length=100, blank= False, null= False )
    apellido= models.TextField(max_length=50, blank= False, null= False)
    nombre = models.TextField(max_length=20, blank= False, null= False )
    usuario= models.TextField(max_length=15, blank= False, null= False )
    contraseña= models.TextField(min_length=8, blank= False, null= False )


    def __str__(self):
        return f'DNI:{self.dni} Correo:{self.correo} Apellido:{self.apellido} Nombre:{self.nombre} Usuario: {self.usuario} Contraseña: {self.contraseña}'

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
    