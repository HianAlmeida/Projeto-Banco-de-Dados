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
    ator = models.ForeignKey(Ator,  on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme,  on_delete=models.CASCADE)

class Cronograma(models.Model):
    id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
    sala_id = models.ForeignKey(Sala,  on_delete=models.CASCADE)    
    filme_id = models.ForeignKey(Filme,  on_delete=models.CASCADE)  
    data_inicio = 
    data_final = 
    horario_inicio = 
    horario_final = 
    


class Cliente(models.Model):
    cpf  = models.CharField(primary_key=True, null=False)
    nome = models.CharField(null=False)



    
    # class Meta:
    #     fields = ["id", "numero", "capacidade"]   