from django.shortcuts import render

# Create your views here.

def gimnasio(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def usuarios(request):
    return render(request, 'base.html')

def registro(request):
    return render(request, 'registro.html')
