# core/views.py
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Usuario
from .models import Pet
from django.contrib import messages
from .forms import PetForm  # Supondo que você tenha um ModelForm baseado no modelo Pet
from django.utils import timezone
from .models import Pet  # ou o modelo correto que você está usando




def sucesso(request):
  return render(request, 'core/sucesso.html')

#def home(request):
#  return render(request, 'core/home.html')

def home(request):
    pet = Pet.objects.first()  # Pega o primeiro pet, ou ajusta a lógica conforme necessário
    return render(request, 'core/home.html', {'pet': pet})



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

def detalhes_usuario(request):
  return render(request, 'core/detalhes_usuario.html')



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






#####################
from django.shortcuts import render, get_object_or_404
from .models import Usuario  # Importe o modelo do usuário


def detalhes_usuario(request, user_id):
    # Busca o usuário pelo ID
    usuario = get_object_or_404(Usuario, id=user_id)

    # Envia os dados do usuário para o template
    return render(request, 'detalhes_usuario.html', {'usuario': usuario})


from django.shortcuts import render, get_object_or_404
from .models import Pet  # Certifique-se de que o modelo Pet está importado

def detalhes_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)  # Busca o pet pelo ID
    return render(request, 'core/detalhes_pet.html', {'pet': pet})


from .models import Usuario, Pet  # Importando o modelo Pet

def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtém todos os usuários
    pets = Pet.objects.all()  # Obtém todos os pets
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios, 'pets': pets})

def pets(request, pet_id):
    try:
        pets = Pet.objects.all()  # Obtém todos os pets
    except Pet.DoesNotExist:
        pet = None  # Caso o pet não exista, pode passar um valor padrão ou mensagem
    return render(request, 'core/pets.html', {'pets': pets})


def detalhes_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'core/detalhes_pet.html', {'pet': pet})

def lista_pets(request):
    pets = Pet.objects.all()  # Obtém todos os pets cadastrados
    return render(request, 'core/lista_pets.html', {'pets': pets})