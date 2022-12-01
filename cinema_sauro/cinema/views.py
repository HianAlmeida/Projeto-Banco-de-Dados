from lzma import FILTER_ARM
from wsgiref import validate
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import FilmeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from datetime import datetime


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

    sala, created = Sala.objects.get_or_create(numero=numero, capacidade=capacidade)
    return Response(data={"sala_id": sala.pk }, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def cadastrar_cronograma(request):
    data = request.data
    
    sala_id = data.get("sala_id")
    sala = Sala.objects.get(pk=sala_id)
    
    filme_id = data.get("filme_id")
    filme = Filme.objects.get(pk=filme_id)

    if sala and filme: 
        cronograma = Cronograma()
        cronograma.data_inicio = datetime.strptime(data.get("data_inicio"), "%d/%m/%Y").date()
        cronograma.data_final = datetime.strptime(data.get("data_final"), "%d/%m/%Y").date()
        cronograma.horario_inicio = datetime.strptime(data.get("horario_inicio"), "%H:%M:%S").time()
        cronograma.horario_final = datetime.strptime(data.get("horario_final"), "%H:%M:%S").time()
        cronograma.sala_id = sala
        cronograma.filme_id = filme
        cronograma.save()
        return Response(status=status.HTTP_201_CREATED)
    else: 
       return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(["POST"])
def cadastrar_compra(request):
    data = request.data
   

