from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuário  # Certifique-se de que este é o nome correto

def home(request):
    return render(request, 'core/home.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        rede_social = request.POST.get('rede_social', '')
        password = request.POST['senha']
        image = request.FILES.get('image')  # Obtém a imagem, se fornecida
        
        # Verifica se o email já existe
        if Usuário.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
            return render(request, 'core/cadastro.html')

        # Cria o usuário no modelo Usuário
        Usuário.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            rede_social=rede_social,
            password=password,  # Aqui a senha será salva diretamente
            image=image
        )

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('home')  # Redireciona para a página inicial

    return render(request, 'core/cadastro.html')

def vitrine(request):
    return render(request, 'core/vitrine.html')

def login(request):
    return render(request, 'core/login.html')  # Certifique-se de que o template existe
