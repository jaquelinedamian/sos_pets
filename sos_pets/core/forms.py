# core/forms.py
from django import forms
from .models import Usuario
from .models import Pet

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'rede_social', 'image']  # Exclua 'user'





class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['tipo', 'nome', 'especie', 'porte', 'cor', 'detalhes', 'data_hora', 'localizacao', 'imagem1', 'imagem2', 'imagem3']
