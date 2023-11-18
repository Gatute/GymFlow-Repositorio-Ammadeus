from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class perfil(models.Model):
    nombre = models.CharField(max_length= 200)

    def __str__(self):
        return self.nombre

class user_list(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, default = 1)
    altura = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200, unique=True)
    peso = models.CharField(max_length= 200)
    

    def __str__(self):
        return self.nombre

