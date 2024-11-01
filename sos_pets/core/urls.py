from django.urls import path
from django.shortcuts import render, redirect
from .forms import UsuarioForm
import core.views as views


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
    path('login/', views.login, name='login'),
    path('anuncios/', views.anuncios, name='anuncios'), 
    path('vitrine-detalhes/', views.vitrine_detalhes, name='vitrine_detalhes'), 
    path('conta/', views.conta, name='conta'), 
    path('faq/', views.faq, name='faq'),
    path('meus-anuncios/', views.meus_anuncios, name='meus_anuncios')


]
