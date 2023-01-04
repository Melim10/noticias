from daw.models import *
from rest_framework import serializers


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ('id', 'titulo', 'descricao', 'data')


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'noticia', 'descricao', 'data')
