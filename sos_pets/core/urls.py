from django.contrib.auth.decorators import login_required
from django.urls import path
from django.shortcuts import render, redirect
from .forms import UsuarioForm
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            # Salva o usuário e redireciona para a página de sucesso
            form.save()
            return redirect('sucesso')  # Redireciona para a URL com nome 'sucesso'
    else:
        form = UsuarioForm()  # Cria uma instância vazia do formulário

    return render(request, 'core/cadastro.html', {'form': form})  # Renderiza a página de cadastro

def sucesso(request):
    return render(request, 'core/sucesso.html')  # Renderiza a página de sucesso






urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro-pets/', views.cadastro_pets, name='cadastro_pets'),
    # Defina as demais rotas
    path('busca/', views.busca, name='busca'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('anuncios/', views.anuncios, name='anuncios'), 
    path('vitrine-detalhes/', views.vitrine_detalhes, name='vitrine_detalhes'), 
    path('conta/', views.conta, name='conta'),
    path('faq/', views.faq, name='faq'),
    path('meus-anuncios/', views.meus_anuncios, name='meus_anuncios'),
    path('sucesso/', views.sucesso, name='sucesso'),

    path('detalhes_usuario/', views.detalhes_usuario, name='detalhes_usuario'),


    path('lista_usuarios/', views.listar_usuarios, name='lista_usuarios'),

    path('detalhes_pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),

    path('pets/', views.pets, name='pets'),

    path('lista_pets/', views.lista_pets, name='lista_pets'),

    path('detalhes_pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),

    path('mapa-pets/', views.mapa_pets, name='mapa_pets'),

    path('admin/', admin.site.urls)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)