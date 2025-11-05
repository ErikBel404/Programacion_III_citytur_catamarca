from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.administracion.models import Recorrido, PuntoTuristico


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("usuario:home"))
        else:
            return render(request, "usuario/login.html", {"msj": "Credenciales incorrectas"})
    return render(request, "usuario/login.html")


def logout_view(request):
    logout(request)
    return render(request, "usuario/login.html", {"msj": "Deslogueado"})
#seccion del home
@login_required 
def home_view(request):
    lista_de_recorridos = Recorrido.objects.all()
    context = {
        'recorridos': lista_de_recorridos
    }
    return render(request, 'home.html', context)

@login_required 
def detalle_recorrido_view(request, recorrido_id):
    recorrido = get_object_or_404(Recorrido, id=recorrido_id)
    puntos = recorrido.puntosTuristicos.all()
    
    context = {
        'recorrido': recorrido,
        'puntos': puntos
    }
    return render(request, 'detalle_recorrido.html', context)

def registro_usuario(request):

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            
            user.tipoUsuario = 'turista' 
            
            user.save()
            
            login(request, user)
            
            messages.success(request, f'¡Cuenta creada exitosamente! Bienvenido, {user.username}.')
            return redirect('usuario/home.html') 
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
            
    else:
        form = RegistroUsuarioForm()
        
    contexto = {
        'form' : form
    }

    return render(request, 'usuario/AgregarUsuario.html', contexto)