from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from daw import models, serializers

# Create your views here.


class NoticiaList(APIView):
    def get(self, request):
        noticia = models.Noticia.objects.all()
        noticia_serializer = serializers.NoticiaSerializer(noticia, many=True)
        return Response(noticia_serializer.data)

    def post(self, request):
        noticia_serializer = serializers.NoticiaSerializer(data=request.data)
        if noticia_serializer.is_valid():
            noticia_serializer.save()
            return Response(noticia_serializer.data, status=status.HTTP_201_CREATED)
        return Response(noticia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticiaDetail(APIView):
    def get(self, request, id):
        noticia = self.get_object(id)
        noticia_serializer = serializers.NoticiaSerializer(noticia)
        return Response(noticia_serializer.data)

    def put(self, request, id):
        noticia = self.get_object(id)
        noticia_serializer = serializers.NoticiaSerializer(
            noticia, data=request.data)
        if noticia_serializer.is_valid():
            noticia_serializer.save()
            return Response(noticia_serializer.data)
        return Response(noticia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        noticia = self.get_object(id)
        noticia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComentarioList(APIView):
    def get(self, request):
        comentario = models.Comentario.objects.all()
        comentario_serializer = serializers.ComentarioSerializer(
            comentario, many=True)
        return Response(comentario_serializer.data)

    def post(self, request):
        comentario_serializer = serializers.ComentarioSerializer(
            data=request.data)
        if comentario_serializer.is_valid():
            comentario_serializer.save()
            return Response(comentario_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comentario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComentarioDetail(APIView):
    def get(self, request, id):
        comentario = self.get_object(id)
        comentario_serializer = serializers.ComentarioSerializer(comentario)
        return Response(comentario_serializer.data)

    def put(self, request, id):
        comentario = self.get_object(id)
        comentario_serializer = serializers.ComentarioSerializer(
            comentario, data=request.data)
        if comentario_serializer.is_valid():
            comentario_serializer.save()
            return Response(comentario_serializer.data)
        return Response(comentario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comentario = self.get_object(id)
        comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
