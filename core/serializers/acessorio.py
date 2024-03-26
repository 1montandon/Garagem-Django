from rest_framework.serializers import ModelSerializer

from core.models import Acessorio

class AcessorioSerializer(ModelSerializer):
    class Meta: 
        model = Acessorio
        fidels = "__all__"