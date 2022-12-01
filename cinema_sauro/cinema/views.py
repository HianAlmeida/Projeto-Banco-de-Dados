from lzma import FILTER_ARM
from wsgiref import validate
from django.shortcuts import render, redirect
from .models import Filme, Ator, Atuacao, Sala
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import FilmeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

# Create your views here.
def createView(request):
    return render(request,'criar_filme.html')


@api_view(["POST"])
def cadastrar_filme(request):
    serializer = FilmeSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        filme = Filme(**serializer.validated_data)
        filme.save()
    return Response(data={"filme_id": filme.pk }, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def cadastrar_atuacao(request):
    #peguei o id do filme e achei o objeto filme
    data = request.data
    filme = Filme.objects.get(pk=data.get('filme_id'))
    # criar os atores
    atores = data.get('atores')
    if atores: 
        for nome in atores: 
            ator, created = Ator.objects.get_or_create(nome = nome)
            Atuacao.objects.get_or_create(ator = ator, filme = filme)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["POST"])
def cadastrar_sala(request):
    numero = request.data.get("numero")
    capacidade = request.data.get("capacidade")

    Sala.objects.get_or_create(numero=numero, capacidade=capacidade)
    return Response(status=status.HTTP_201_CREATED)

@api_view(["POST"])
def cadastrar_ingresso(request):
    valor = request.data.get("valor")
    categoria = request.data.get("categoria")
    data = request.data.get("data")
    id_cronograma = data.get("id_cronograma")
    cronograma = Cronograma.objects.get(pk=cronograma_id)

    Ingresso.objects.get_or_create(valor=valor, categoria=categoria, data=data, id_cronograma=id_cronograma)