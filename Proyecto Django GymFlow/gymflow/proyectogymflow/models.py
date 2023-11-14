from django.db import models

# Create your models here.

class perfil(models.Model):
    nombre = models.CharField(max_length= 200)

    def __str__(self):
        return self.nombre

class user_list(models.Model):
    altura = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200, unique=True)
    peso = models.CharField(max_length= 200)
    

    def __str__(self):
        return self.nombre

