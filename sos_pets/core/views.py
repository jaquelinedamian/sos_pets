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
from decimal import Decimal
import requests

def sucesso(request):
    return render(request, 'core/sucesso.html')

def home(request):
    pet = Pet.objects.first()  # Pega o primeiro pet, ou ajuste conforme necessário
    return render(request, 'core/home.html', {'pet': pet})

def busca(request):
    pets = Pet.objects.all()
    return render(request, 'core/busca.html', {'pets': pets})



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
    if request.user.is_authenticated:
        return redirect('conta')

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
            return redirect('/')  # Redireciona para a página de sucesso
        else:
            messages.error(request, 'Erro no cadastro do pet. Verifique as informações e tente novamente.')
            for field, errors in form.errors.items():
                print(f"Campo {field}: {errors}")

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
    return render(request, 'core/detalhes_pet.html', {
        'pet': pet,
        'LOCATIONIQ_API_KEY': settings.LOCATIONIQ_API_KEY  # Passando a chave da API para o template
    })



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





import requests
from django.shortcuts import render

def reverse_geocode(request):
    # Token da API do LocationIQ
    api_token = "pk.227bb16be8af10a97550047d4932e148"

    # Latitude e longitude (exemplo)
    latitude = request.GET.get('lat', '-23.55052')  # Default: São Paulo
    longitude = request.GET.get('lon', '-46.633308')  # Default: São Paulo

    # URL da API
    url = f"https://eu1.locationiq.com/v1/reverse.php?key={api_token}&lat={latitude}&lon={longitude}&format=json"

    # Requisição à API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Gera erro se a requisição falhar
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = {"error": str(e)}

    return render(request, 'core/mapa.html', {'location_data': data})

