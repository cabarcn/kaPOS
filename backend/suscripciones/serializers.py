from rest_framework import serializers
from .models import Suscripcion, EventoSuscripcion

class EventoSuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoSuscripcion
        fields = ['id', 'suscripcion', 'tipo', 'detalle', 'metadata', 'actor', 'created_at']


class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = '__all__'
        read_only_fields = ['monto_suscrito', 'created_at', 'updated_at']
