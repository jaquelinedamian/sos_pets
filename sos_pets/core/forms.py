# core/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nome', 'email', 'telefone', 'rede_social', 'image']  # Exclua 'user'
