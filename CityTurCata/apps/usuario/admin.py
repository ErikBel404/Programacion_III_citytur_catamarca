from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register (Usuario)
class UsuarioAdmin (UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('documento_identidad', 'domicilio', 'tipoUsuario')}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('documento_identidad', 'domicilio', 'tipoUsuario')}),)
    



