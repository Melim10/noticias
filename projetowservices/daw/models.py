from django.db import models

# Create your models here.


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)


class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
