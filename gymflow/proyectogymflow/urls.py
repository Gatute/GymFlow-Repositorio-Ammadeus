from django.urls import path 
from .views import gimnasio, inicio, perfil, usuarios, registro

urlpatterns = [
    path('gimnasio', gimnasio, name="gimnasio"),
    path('gimnasio/inicio', inicio, name="inicio"),
    path('gimnasio/perfil', perfil, name='perfil'),
    path('gimnasio/usuarios', usuarios, name='usuarios'),
    path('gimnasio/registro', registro, name='registro')
] 