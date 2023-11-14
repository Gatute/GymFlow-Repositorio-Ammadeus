from django.urls import path 
from .views import login, inicio, perfil, base , registro, lista_usuarios, user_logeo

urlpatterns = [
    path('gimnasio/logeo', user_logeo, name="login"), # Funcion para logearse
    path('', login, name="gimnasio"),
    path('gimnasio/inicio', inicio, name="inicio"),
    path('gimnasio/perfil', perfil, name='perfil'),
    path('gimnasio/base', base, name='usuarios'),
    path('gimnasio/registro', registro, name='registro'),
    path('gimnasio/usuarios', lista_usuarios, name='lista_usuarios')
    
] 