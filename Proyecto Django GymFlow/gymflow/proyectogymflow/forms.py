from django import forms
from .models import user_list

class informacion_perfil_usuario(forms.ModelForm):
    class Meta:
        model = user_list
        fields = ['altura', 'nombre', 'peso', 'nivel_actividad']
