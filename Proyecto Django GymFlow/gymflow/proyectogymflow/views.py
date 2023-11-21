from django.shortcuts import render, redirect
from .models import perfil_usuario_login, user_list
from .forms import informacion_perfil_usuario
from django.contrib.auth import login as Funcion_django_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'index.html')

def perfil(request):
    usuarios = user_list.objects.all() ##Select * from usuario
    
    context = {
        'usuarios' : usuarios 
    }

    return render(request, 'perfil.html', context)

def base(request):
    return render(request, 'base.html') 

def registro(request):
    return render(request, 'registro.html')

def rutina(request):
    return render(request, 'rutina.html')

def rutina(request):
    return render(request, 'maquinas.html')

def lista_usuarios(request):

    usuarios = user_list.objects.all() ##Select * from usuario
    
    context = {
        'usuarios' : usuarios 
    }

    return render(request, 'Usuarios/lista_usuarios.html', context)

def user_logeo(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('pass')

        # Check if both fields are not empty
        if usuario and clave:
            user = authenticate(request, username=usuario, password=clave)

            if user is not None:
                profile = perfil_usuario_login.objects.get(user=user)
                request.session['perfil'] = profile.role

                Funcion_django_login(request, user)
                return redirect('inicio')
            else:
                context = {
                    'error': 'Error intente nuevamente.'
                }
                return render(request, 'login.html', context)
        else:
            context = {
                'error': 'Ambos campos son obligatorios. Por favor, inténtelo nuevamente.'
            }
            return render(request, 'login.html', context)

    return render(request, '')


