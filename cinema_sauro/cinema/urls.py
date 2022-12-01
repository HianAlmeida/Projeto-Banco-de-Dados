from django.urls import path
from .views import *



urlpatterns = [
    path('create',createView),
    path('cadastra_filme',cadastrar_filme,),
    path('cadastrar_atuacao', cadastrar_atuacao),
    path('cadastrar_sala', cadastrar_sala),
    path('cadastrar_ingresso', cadastrar_ingresso)

    path('cadastrar_cronograma', cadastrar_cronograma),
    path('cadastrar_compra', cadastrar_compra)
]