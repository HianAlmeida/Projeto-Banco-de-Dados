from rest_framework.serializers import ModelSerializer, BooleanField
from .models import Filme

class FilmeSerializer(ModelSerializer):
    nacional = BooleanField(required=False)

    class Meta:
        model = Filme
        fields = ["nome", "categoria", "empresa_produtora", "nacional", "censura", "duracao"]

    def validate(self, data):
        data["nacional"] = True if data.get("nacional") else False

        return super().validate(data)
              

