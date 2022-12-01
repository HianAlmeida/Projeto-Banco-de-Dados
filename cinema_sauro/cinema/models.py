from django.db import models
from uuid import uuid4

# Create your models here.
class Sala(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    numero =  models.CharField(null=False, max_length=5) 
    capacidade = models.IntegerField(null=False)

class Filme(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    nome =  models.CharField(null=False, max_length=255) 
    categoria = models.CharField(null=False, max_length=255)
    empresa_produtora = models.CharField(null=False, max_length=255) 
    nacional = models.BooleanField(null=False) 
    censura = models.CharField(null=False, max_length=255) 
    duracao = models.IntegerField(null=False) 

class Ator(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    nome =  models.CharField(null=False, max_length=255)

class Atuacao(models.Model): 
    id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
    ator = models.ForeignKey(Ator,  on_delete=models.CASCADE, null=False)
    filme = models.ForeignKey(Filme,  on_delete=models.CASCADE, null=False)

class Cronograma(models.Model):
    id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
    sala_id = models.ForeignKey(Sala,  on_delete=models.CASCADE, null=False)    
    filme_id = models.ForeignKey(Filme,  on_delete=models.CASCADE, null=False)  
    data_inicio = models.DateField(auto_now=False, null=False)
    data_final =  models.DateField(auto_now=False, null=False)
    horario_inicio = models.TimeField(auto_now=False, null=False)
    horario_final = models.TimeField(auto_now=False, null=False)

class Ingresso(models.Model):
    id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
    valor = models.FloatField(null=False)
    categoria = models.CharField(null=False, max_length=255)
    id_cronograma = models.ForeignKey(Cronograma, null=False, on_delete=models.CASCADE)  
    data = models.DateField(auto_now=False)

class Cliente(models.Model):
<<<<<<< HEAD
    cpf  = models.CharField(primary_key=True, null=False, max_length=255)
    nome = models.CharField(null=False, max_length=255)
=======
    cpf  = models.CharField(primary_key=True, null=False, max_length=250)
    nome = models.CharField(null=False, max_length=250)
>>>>>>> f1f33c27dba90afa54f47868b243094fcafdea25

class ItemLanchonete(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    nome = models.CharField(null=False, max_length=255)
    valor = models.FloatField(null=False)

class Compra(models.Model):
    id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
    cpf_cliente = models.ForeignKey(Cliente,  on_delete=models.CASCADE)  
    data = models.DateField(auto_now=True)

class CompraIngressos(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    id_compra = models.ForeignKey(Compra,  on_delete=models.CASCADE)
    id_ingresso = models.ForeignKey(Ingresso,  on_delete=models.CASCADE)

class CompraProdutos(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    id_compra = models.ForeignKey(Compra,  on_delete=models.CASCADE)
    id_produto = models.ForeignKey(ItemLanchonete,  on_delete=models.CASCADE)
