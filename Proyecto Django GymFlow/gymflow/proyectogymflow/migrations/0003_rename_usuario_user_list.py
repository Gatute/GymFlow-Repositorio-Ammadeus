# Generated by Django 4.2.6 on 2023-10-31 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectogymflow', '0002_remove_usuario_categoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuario',
            new_name='user_list',
        ),
    ]
