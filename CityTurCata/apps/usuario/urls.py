from django.urls import path
from apps.usuario import views

app_name = 'usuario'

urlpatterns = [
    path('usuarios/login/', views.login_view, name='login'),
    path('usuarios/logout/',views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('recorrido/<int:recorrido_id>/', views.detalle_recorrido_view, name='detalle_recorrido'),
    path('usuarios/agregar/',views.registro_usuario, name='registroUsuario'),
]