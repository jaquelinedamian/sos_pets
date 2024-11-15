# core/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Usuario, Pet
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def sucesso(request):
    return render(request, 'core/sucesso.html')

def home(request):
    pet = Pet.objects.first()  # Pega o primeiro pet, ou ajuste conforme necessário
    return render(request, 'core/home.html', {'pet': pet})

def busca(request):
    return render(request, 'core/busca.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('conta')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
            else:
                messages.error(request, "Credenciais inválidas.")
        else:
            messages.error(request, "Erro no formulário. Verifique os campos e tente novamente.")
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Ou redirecione para onde achar necessário


def anuncios(request):
    return render(request, 'core/anuncios.html')

def vitrine_detalhes(request):
    return render(request, 'core/vitrine-detalhes.html')

@login_required
def conta(request):
    return render(request, 'core/conta.html')

def faq(request):
    return render(request, 'core/faq.html')

@login_required
def meus_anuncios(request):
    return render(request, 'core/meus-anuncios.html')

def cadastro(request):
    if request.method == 'POST':
        senha = request.POST['senha']
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        rede_social = request.POST.get('rede_social', '')
        image = request.FILES['foto']

        # Cria o usuário usando o email como username
        user = User.objects.create_user(username=email, email=email, password=senha)

        # Cria o perfil do usuário
        Usuario.objects.create(nome=nome, email=email, telefone=telefone, rede_social=rede_social, image=image, usuario=user)

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('home')

    return render(request, 'core/cadastro.html')

@login_required
def cadastro_pets(request):
    # Se for um POST, processa o formulário
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            # Você pode adicionar qualquer lógica extra aqui (como data/hora ou outras verificações)
            pet.save()
            messages.success(request, 'Pet cadastrado com sucesso!')
            return redirect('sucesso.html')  # Redireciona para a página de sucesso
        else:
            messages.error(request, 'Erro no cadastro do pet. Verifique as informações e tente novamente.')

    # Se for um GET, apenas exibe o formulário
    else:
        form = PetForm()

    # Passando o formulário e a chave de API para o template
    return render(request, 'core/cadastro-pets.html', {
        'form': form,
        'LOCATIONIQ_API_KEY': settings.LOCATIONIQ_API_KEY  # Passando a chave da API para o template
    })

@login_required
def detalhes_usuario(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    return render(request, 'core/detalhes_usuario.html', {'usuario': usuario})

def detalhes_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'core/detalhes_pet.html', {'pet': pet})

@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    pets = Pet.objects.all()
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios, 'pets': pets})

def pets(request, pet_id):
    pets = Pet.objects.all()
    return render(request, 'core/pets.html', {'pets': pets})

def lista_pets(request):
    pets = Pet.objects.all()
    return render(request, 'core/lista_pets.html', {'pets': pets})

def mapa_pets(request):
    pets = Pet.objects.all()
    return render(request, 'core/mapa_pets.html', {'pets': pets})