from django.db import models


class Usuário(models.Model):  # Nome da classe ajustado
    nome = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('Email do usuário', unique=True)
    telefone = models.CharField('Telefone', max_length=20)
    rede_social = models.CharField('Rede social principal', max_length=100, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True)
    senha = models.CharField('Senha', max_length=100)

    def __str__(self):
        return self.nome
