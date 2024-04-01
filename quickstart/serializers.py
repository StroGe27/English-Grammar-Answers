from quickstart.models import RouteToRes
from rest_framework import serializers

class RouteToResSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = RouteToRes
        # Поля, которые мы сериализуем
        fields = [
            "payload",
        ]
