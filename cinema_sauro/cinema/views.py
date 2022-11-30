from lzma import FILTER_ARM
from wsgiref import validate
from django.shortcuts import render, redirect
from .models import Filme
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import FilmeSerializer

# Create your views here.
def createView(request):
    return render(request,'criar_filme.html')


@api_view(["POST"])
def filme(request):
    serializer = FilmeSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        filme = Filme(**serializer.validated_data)
        filme.save()
    messages.success(request, "Filme criado com sucesso")
    return redirect('/cinema/create')