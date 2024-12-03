# core/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nome = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('Email do usuário', unique=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    rede_social = models.CharField('Rede social principal', max_length=100, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', null=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"

class Pet(models.Model):
    TIPOS_CHOICES = [
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
    ]

    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
    ]

    PORTE_CHOICES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ]

    # Altere o campo usuario para incluir um valor default
    usuario = models.ForeignKey(
        'Usuario',  # Substitua por settings.AUTH_USER_MODEL se Usuario for o usuário padrão
        on_delete=models.CASCADE,
        related_name='pets',
        verbose_name='Dono',
        null=True,  # Permite valores nulos para os registros antigos
        blank=True,  # Permite valores vazios no formulário
        default=None  # Aqui você pode adicionar um valor default (como um usuário específico)
    )
    tipo = models.CharField('Tipo', max_length=10, choices=TIPOS_CHOICES)
    nome = models.CharField('Nome do Pet', max_length=100)
    especie = models.CharField('Espécie', max_length=10, choices=ESPECIE_CHOICES)
    porte = models.CharField('Porte', max_length=10, choices=PORTE_CHOICES)
    cor = models.CharField('Cor', max_length=30)
    detalhes = models.TextField('Detalhes', blank=True)
    data_hora = models.DateTimeField('Data e Hora')  # Permite ao usuário definir data e hora
    localizacao = models.CharField('Descrição do Local', max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)  # Novo campo

    latitude = models.DecimalField('Latitude', max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField('Longitude', max_digits=9, decimal_places=6, blank=True, null=True)
    telefone_contato = models.CharField('Telefone do Tutor', max_length=15, blank=True)
    email_contato = models.EmailField('E-mail do Tutor', blank=True)
    imagem1 = models.ImageField(upload_to='pets/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='pets/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='pets/', blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - {self.tipo}'

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
