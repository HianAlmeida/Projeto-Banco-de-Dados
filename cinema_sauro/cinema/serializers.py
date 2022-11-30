from rest_framework.serializers import ModelSerializer, BooleanField, UUIDField, ListField
from .models import Filme, Ator

class FilmeSerializer(ModelSerializer):
    nacional = BooleanField(required=False)

    class Meta:
        model = Filme
        fields = ["nome", "categoria", "empresa_produtora", "nacional", "censura", "duracao"]

    def validate(self, data):
        data["nacional"] = True if data.get("nacional") else False

        return super().validate(data)

# class AtuacaoSerializer(ModelSerializer):
#     filme_id = UUIDField(required=True)
#     nome = serializers.ListField(
#     child = serializers.CharField(min_value = 0, max_value = 100)
#     )

#     class Meta: 
#         model = Ator
#         fields = ["nome", "filme_id"]

