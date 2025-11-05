# apps/usuario/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db import transaction
from django.conf import settings
User = settings.AUTH_USER_MODEL 

def asignar_grupo_turista(user_instance):
    """Función que realiza la asignación de grupo."""
    try:
        grupo_turista = Group.objects.get(name='turista')
        user_instance.groups.add(grupo_turista) 
  

    except Group.DoesNotExist:
        print("ADVERTENCIA: El grupo 'turista' no existe en la base de datos.")


@receiver(post_save, sender=User)
def manejar_creacion_usuario(sender, instance, created, **kwargs):
    if created:
  
        if instance.tipoUsuario == 'turista':
            
            transaction.on_commit(lambda: asignar_grupo_turista(instance))