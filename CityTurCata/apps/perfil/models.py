from django.db import models

# Create your models here.
class Persona(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    correo = models.TextField(max_length=100)
    apellido= models.TextField(max_length=50)
    nombre = models.TextField(max_length=20)
    usuario= models.TextField(max_length=15)
    contraseña= models.TextField(min_length=8)

    def __str__(self):
        return f'DNI:{self.dni} Correo:{self.correo} Apellido:{self.apellido} Nombre:{self.nombre} Usuario: {self.usuario} Contraseña: {self.contraseña}'

class Administrador (models.Model):
    domicilio = models.TextField(max_length=50)
    categoria = models.TextField(max_length=20)
    estado = models.TextField(max_length=15)

    def __str__(self):
        return f'Domicilio:{self.domicilio} Categoria:{self.categoria} Estado:{self.estado}'

class Cliente(models.Model):

    nombreInstitucion = models.TextField(max_length=100)
    cuit= models.TextField(ax_length=11)

    def __str__(self):
        return f'Nombre Institucion: {self.nombreInstitucion} Cuit:{self.cuit}'

class Operario(models.Model):
    domicilio = models.TextField(max_length=50)
    categoria = models.TextField(max_length=20)

    def __str__(self):
        return f'Domicilio:{self.domicilio} Categoria:{self.categoria}'
    
class Turista(models.Model):
    cantGrupoFamiliar= models.IntegerChoices()
    def __str__(self):
        return f'Cantidad del grupo familiar:{self.cantGrupoFamiliar}'