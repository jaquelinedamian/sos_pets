from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirme a senha')

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'rede_social', 'image', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        senha_confirm = cleaned_data.get("senha_confirm")

        if senha != senha_confirm:
            self.add_error('senha_confirm', "As senhas não coincidem.")
