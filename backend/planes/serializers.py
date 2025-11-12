from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Plan
    """
    periodicidad_display = serializers.CharField(
        source='get_periodicidad_display',
        read_only=True
    )
    
    class Meta:
        model = Plan
        fields = [
            'id', 'nombre', 'descripcion', 'monto', 
            'periodicidad', 'periodicidad_display',
            'dia_cobro', 'activo', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_monto(self, value):
        """
        Validar que el monto sea positivo
        """
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor a 0")
        return value
    
    def validate_dia_cobro(self, value):
        """
        Validar día de cobro
        """
        if value < 1 or value > 28:
            raise serializers.ValidationError("El día de cobro debe estar entre 1 y 28")
        return value


class PlanListSerializer(serializers.ModelSerializer):
    """
    Serializador simplificado para listar planes (solo activos)
    """
    periodicidad_display = serializers.CharField(
        source='get_periodicidad_display',
        read_only=True
    )
    
    class Meta:
        model = Plan
        fields = ['id', 'nombre', 'monto', 'periodicidad', 'periodicidad_display']