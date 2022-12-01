from django.urls import path
from .views import createView, cadastrar_filme, cadastrar_atuacao, cadastrar_sala, cadastrar_ingresso



urlpatterns = [
    path('create',createView),
    path('cadastra_filme',cadastrar_filme,),
    path('cadastrar_atuacao', cadastrar_atuacao),
    path('cadastrar_sala', cadastrar_sala),
    path('cadastrar_ingresso', cadastrar_ingresso)

]