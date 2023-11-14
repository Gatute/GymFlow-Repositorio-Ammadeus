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

def lista_usuarios(request):

    usuarios = user_list.objects.all() ##Select * from usuario
    
    context = {
        'usuarios' : usuarios 
    }

    return render(request, 'Usuarios/lista_usuarios.html', context)



# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index.html')  # replace 'home' with your desired home page URL
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def user_logeo(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             # Authenticate the user
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 # Login the user
#                 login(request, user)
#                 return redirect('inicio')  # replace 'home' with your desired home page URL
#     else:
#         form = AuthenticationForm()

#     return render(request, 'index.html', {'form': form})

# def user_logeo(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             # Check if both username and password are provided
#             if form.cleaned_data.get('username') and form.cleaned_data.get('password'):
#                 # Authenticate the user
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = authenticate(request, username=username, password=password)

#                 if user is not None:
#                     # Login the user
#                     login(request, user)
#                     return redirect('inicio')  # replace 'home' with your desired home page URL
#             else:
#                 form.add_error(None, 'Please provide both username and password.')
#     else:
#         form = AuthenticationForm()

#     return render(request, 'index.html', {'form': form})

# def user_logeo(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             # Check if both username and password are provided
#             if form.cleaned_data.get('username') and form.cleaned_data.get('password'):
#                 # Authenticate the user
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = authenticate(request, username=username, password=password)

#                 if user is not None:
#                     # Login the user
#                     login(request, user)
#                     return redirect('inicio')  # replace 'home' with your desired home page URL
#             else:
#                 form.add_error(None, 'Please provide both username and password.')
#     else:
#         form = AuthenticationForm()

#     return render(request, 'index.html', {'form': form})


def user_logeo(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Check if both username and password are provided
            if form.cleaned_data.get('username') and form.cleaned_data.get('password'):
                # Authenticate the user
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    # Login the user
                    login(request, user)
                    return redirect('inicio')  # replace 'home' with your desired home page URL
            else:
                form.add_error(None, 'Please provide both username and password.')
    else:
        form = AuthenticationForm()

    return render(request, 'index.html', {'form': form})