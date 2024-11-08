# core/views.py
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Usuario
from .models import Pet
from django.contrib import messages
from .forms import PetForm  # Supondo que você tenha um ModelForm baseado no modelo Pet
from django.utils import timezone



def sucesso(request):
  return render(request, 'core/sucesso.html')

def home(request):
  return render(request, 'core/home.html')

def busca(request):
  return render(request, 'core/busca.html')

def login(request):
  return render(request, 'core/login.html')



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






def cadastro_pets__(request):
  return render(request, 'core/cadastro-pets.html')




def cadastro_pets(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        nome = request.POST['nome']
        especie = request.POST['especie']
        porte = request.POST['porte']
        cor = request.POST['cor']
        detalhes = request.POST['detalhes']
        data_hora = request.POST.get('data_hora') or timezone.now()  # Usa a data/hora atual se não fornecida
        localizacao = request.POST['localizacao']

        # Captura as imagens
        imagem1 = request.FILES.get('imagem1', None)
        imagem2 = request.FILES.get('imagem2', None)
        imagem3 = request.FILES.get('imagem3', None)

        # Tenta criar a instância do modelo Pet com os dados capturados
        try:
            Pet.objects.create(
                tipo=tipo,
                nome=nome,
                especie=especie,
                porte=porte,
                cor=cor,
                detalhes=detalhes,
                data_hora=data_hora,
                localizacao=localizacao,
                imagem1=imagem1,
                imagem2=imagem2,
                imagem3=imagem3
            )
            # Exibe mensagem de sucesso e redireciona
            messages.success(request, 'Pet cadastrado com sucesso!')
            return redirect('sucesso.html')  # Redireciona para a URL configurada
        except Exception as e:
            # Em caso de erro, exibe mensagem de erro e loga o problema para revisão
            messages.error(request, f'Ocorreu um erro no cadastro do pet: {e}')

    return render(request, 'core/cadastro-pets.html')






