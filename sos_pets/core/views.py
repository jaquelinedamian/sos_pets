# core/views.py
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm  # Certifique-se de que isso está correto
from .models import Usuario
from django.contrib import messages



def sucesso(request):
  return render(request, 'core/sucesso.html')

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
        senha = request.POST['senha']
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        rede_social = request.POST.get('rede_social', '')



        # Cria o usuário usando o email como username
        user = User.objects.create_user(username=email,  email=email, password=senha)

        # Cria o perfil do usuário
        Usuario.objects.create(nome=nome, email=email, telefone=telefone, rede_social=rede_social)

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('home')  # Redireciona para a página inicial

    return render(request, 'core/cadastro.html')