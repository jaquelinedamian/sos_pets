# core/admin.py

from django.contrib import admin
from .models import Usuário  # Importando o modelo Usuário

# Registra o modelo Usuário para que seja visível no admin
admin.site.register(Usuário)
