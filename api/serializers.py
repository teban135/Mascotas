from rest_framework import serializers
from .models import Mascotas

class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = '__all__'