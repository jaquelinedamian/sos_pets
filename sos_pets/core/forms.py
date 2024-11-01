# core/forms.py
from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'email', 'telefone', 'rede_social', 'image']  # Exclua 'user'
