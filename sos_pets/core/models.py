
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nome = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('Email do usuário', unique=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    rede_social = models.CharField('Rede social principal', max_length=100, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True)
    senha = models.CharField('Senha', max_length=100)

    def save(self, *args, **kwargs):
        # Hash a senha antes de salvar
        if self.senha:
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

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

    tipo = models.CharField('Tipo', max_length=10, choices=TIPOS_CHOICES)
    nome = models.CharField('Nome do Pet', max_length=100)
    especie = models.CharField('Espécie', max_length=10, choices=ESPECIE_CHOICES)
    porte = models.CharField('Porte', max_length=10, choices=PORTE_CHOICES)
    cor = models.CharField('Cor', max_length=30)
    detalhes = models.TextField('Detalhes')
    data_hora = models.DateTimeField('Data e Hora')
    localizacao = models.CharField('Localização', max_length=255)
    imagem1 = models.ImageField(upload_to='pets/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='pets/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='pets/', blank=True, null=True)


    def __str__(self):
        return f'{self.nome} - {self.tipo}'

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'



