# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm  # Certifique-se de que isso está correto
from .models import Usuario
from django.contrib import messages


def home(request):
  return render(request, 'core/home.html')

def busca(request):
  return render(request, 'core/busca.html')

def login(request):
  return render(request, 'core/login.html')

def cadastro_pets(request):
  return render(request, 'core/cadastro-pets.html')

def anuncios(request):
  return render(request, 'core/anuncios.html')

def vitrine_detalhes(request):
  return render(request, 'core/vitrine-detalhes.html')

def conta(request):
  return render(request, 'core/conta.html')

def faq(request):
  return render(request, 'core/faq.html')

def meus_anuncios(request):
  return render(request, 'core/meus-anuncios.html')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        rede_social = request.POST.get('rede_social', '')

        # Verifica se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return render(request, 'core/cadastro.html')

        # Cria o usuário
        user = User.objects.create_user(username=username, password=password, email=email)

        # Cria o perfil do usuário
        Usuario.objects.create(user=user, nome=nome, email=email, telefone=telefone, rede_social=rede_social)

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('home')  # Redireciona para a página inicial

    return render(request, 'core/cadastro.html')
