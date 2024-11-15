# core/forms.py
from django import forms
from .models import Usuario, Pet

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'rede_social', 'image']  # Exclua 'user' caso não seja necessário

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'tipo', 'nome', 'especie', 'porte', 'cor', 'detalhes',
            'data_hora', 'localizacao', 'latitude', 'longitude',
            'telefone_contato', 'email_contato', 'imagem1', 'imagem2', 'imagem3'
        ]
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
