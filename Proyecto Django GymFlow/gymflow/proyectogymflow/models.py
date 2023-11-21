from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class perfil_usuario_login(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, default = 1)
    role = models.CharField(max_length=20, choices=settings.ROLES, default = 1)
    def __str__(self):
        return self.user.username + ' - ' + self.role

class user_list(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = 1)
    altura = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200, unique=True)
    peso = models.CharField(max_length= 200)
    nivel_actividad = models.CharField(max_length=50, default='sedentario')

    
    def __str__(self):
            return self.nombre
    

