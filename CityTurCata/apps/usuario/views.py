from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistroUsuarioForm
from django.contrib import messages



# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("usuario/home.html"))
        else:
            return render(request, "usuario/login.html", {"msj": "Credenciales incorrectas"})
    return render(request, "usuario/login.html")


def logout_view(request):
    logout(request)
    return render(request, "usuario/login.html", {"msj": "Deslogueado"})



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