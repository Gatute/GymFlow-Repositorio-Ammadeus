from django.shortcuts import render, redirect
from .models import user_list
from .forms import User
from django.contrib.auth import login as Funcion_django_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def login(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def base(request):
    return render(request, 'base.html') 

def registro(request):
    return render(request, 'registro.html')

def rutina(request):
    return render(request, 'rutina.html')

def lista_usuarios(request):

    usuarios = user_list.objects.all() ##Select * from usuario
    
    context = {
        'usuarios' : usuarios 
    }

    return render(request, 'Usuarios/lista_usuarios.html', context)

# def user_logeo(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             # Revisa si el usuario y contraseña se usaron
#             if form.cleaned_data.get('username') and form.cleaned_data.get('password'):
#                 # Auntentica al usuario
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = authenticate(request, username=username, password=password)

#                 if user is not None:
#                     # Ingresa al usuario
#                     login(request, user)
#                     return redirect('inicio')  
#             else:
#                 form.add_error(None, 'Por favor ingrese usuario y contraseña.')
#     else:
#         form = AuthenticationForm()

#     return render(request, 'index.html', {'form': form})

# def user_logeo(request):
#     if request.method == 'POST':
#         usuario = request.POST.get('usuario')
#         clave = request.POST.get('pass')
#         user = authenticate(request, username=usuario, password=clave)
        
#         if usuario and clave:
#             user = authenticate(request, username=usuario, password=clave)

#             if user is not None:
#                 profile = user_list.objects.get(user=user)
#                 request.session['perfil'] = profile.role

#                 login(request, user)
#                 return redirect('inicio')
#             else:
#                 context = {
#                     'error' : 'Error intente nuevamente.'
#                 }
#                 return render(request, 'index.html', context)

#     return render(request, 'index.html')


def user_logeo(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('pass')

        # Check if both fields are not empty
        if usuario and clave:
            user = authenticate(request, username=usuario, password=clave)

            if user is not None:
                profile = user_list.objects.get(user=user)
                request.session['perfil'] = profile.role

                login(request, user)
                return redirect('inicio')
            else:
                context = {
                    'error': 'Error intente nuevamente.'
                }
                return render(request, 'index.html', context)
        else:
            context = {
                'error': 'Ambos campos son obligatorios. Por favor, inténtelo nuevamente.'
            }
            return render(request, 'index.html', context)

    return render(request, '')
