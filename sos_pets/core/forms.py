# core/forms.py
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'rede_social', 'image']  # Exclua 'user'
