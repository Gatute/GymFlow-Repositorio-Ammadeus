# Generated by Django 4.2.3 on 2023-11-20 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectogymflow', '0004_user_list_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='user_list',
            name='user',
        ),
        migrations.AddField(
            model_name='perfil',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrador'), ('cliente', 'Cliente')], default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user_list',
            name='nivel_actividad',
            field=models.CharField(default='sedentario', max_length=50),
        ),
    ]
