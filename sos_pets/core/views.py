
from .models import Pet

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm

def cadastro(request):
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






def cadastrar_pet(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        nome = request.POST['nome']
        especie = request.POST['especie']
        porte = request.POST['porte']
        cor = request.POST['cor']
        detalhes = request.POST['detalhes']
        data_hora = request.POST['data_hora']  # Você pode usar um widget de data/hora no seu formulário
        localizacao = request.POST['localizacao']
        imagem1 = request.FILES.get('imagem1')  # Obtém a imagem 1, se fornecida
        imagem2 = request.FILES.get('imagem2')  # Obtém a imagem 2, se fornecida
        imagem3 = request.FILES.get('imagem3')  # Obtém a imagem 3, se fornecida
        
        # Cria o pet no modelo Pet
        pet = Pet.objects.create(
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

        messages.success(request, "Pet cadastrado com sucesso!")
        return redirect('meus_anuncios')  # Altere para o nome correto da sua URL

    return render(request, 'pets/cadastro.html')





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




