from django.contrib import admin
from .models import Usuario, Pet  # Importando os modelos Usuário e Pet

# Personalizando a exibição do modelo Usuario no admin
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'rede_social')  # Campos para exibição na listagem
    search_fields = ('nome', 'email')  # Permite pesquisa por nome e email
    list_filter = ('rede_social',)  # Filtro por rede social

# Personalizando a exibição do modelo Pet no admin
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'especie', 'porte', 'cor', 'localizacao', 'data_hora')  # Campos para exibição na listagem
    search_fields = ('nome', 'tipo', 'especie')  # Permite pesquisa por nome, tipo e espécie
    list_filter = ('tipo', 'porte', 'especie')  # Filtro por tipo, porte e espécie

# Registrando os modelos com suas configurações personalizadas
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pet, PetAdmin)
