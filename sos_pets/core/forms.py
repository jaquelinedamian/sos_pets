from django import forms
from .models import Usuário  # Atualizado para o novo nome do modelo

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuário
        fields = ['nome', 'email', 'telefone', 'rede_social', 'image', 'password']
