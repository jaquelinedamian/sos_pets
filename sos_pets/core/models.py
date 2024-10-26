# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    user_id = models.CharField('Nome do usuário', max_length=20)
    nome = models.CharField('Nome completo do usuário que possui user id',max_length=100)
    email = models.EmailField('Email do usuário')
    telefone = models.CharField('Telefone do usuário', max_length=20)
    rede_social = models.CharField('Rede social principal', max_length=100, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True)

    def __str__(self):
        return self.nome


