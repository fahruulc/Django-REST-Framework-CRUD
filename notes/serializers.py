from rest_framework import serializers
from .models import Penulis, Catatan


class PenulisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penulis
        fields = '__all__'


class CatatanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catatan
        fields = '__all__'
