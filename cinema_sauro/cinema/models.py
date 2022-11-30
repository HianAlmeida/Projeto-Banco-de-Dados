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

# class Cronograma(models.Model):
#     id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
#     sala_id = models.ForeignKey(Sala,  on_delete=models.CASCADE)    
#     filme_id = models.ForeignKey(Filme,  on_delete=models.CASCADE)  
#     # data_inicio = 
#     # data_final = 
#     # horario_inicio = 
#     # horario_final = 

# class Ingresso(models.Model):
#     id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
#     valor = models.FloatField(null=False)
#     categorial = models.CharField(null=False, max_length=255)
#     id_cronograma = models.ForeignKey(Cronograma,  on_delete=models.CASCADE)  
#     # data = 
    


# # class Cliente(models.Model):
# #     cpf  = models.CharField(primary_key=True, null=False)
# #     nome = models.CharField(null=False)

# class ItemLanchonete(models.Model):
#     id = id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
#     nome = models.CharField(null=False, max_length=255)
#     valor = models.FloatField(null=False)

# # class Compra(models.Model):
# #     id = id  = models.UUIDField(primary_key=True, null=False, default=uuid4)
# #     cpf_cliente = models.ForeignKey(Cliente,  on_delete=models.CASCADE)  
# #     # data = 

# class CompraIngressos(models.Model):
#     id = models.UUIDField(primary_key=True, null=False, default=uuid4)
#     id_compra = models.ForeignKey(Compra,  on_delete=models.CASCADE)
#     id_ingresso = models.ForeignKey(Ingresso,  on_delete=models.CASCADE)


# class CompraProdutos(models.Model):
#     id = models.UUIDField(primary_key=True, null=False, default=uuid4)
#     id_compra = models.ForeignKey(Compra,  on_delete=models.CASCADE)
#     id_produto = models.ForeignKey(ItemLanchonete,  on_delete=models.CASCADE)
