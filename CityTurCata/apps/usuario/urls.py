from django.urls import path
from apps.usuario import views

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
]