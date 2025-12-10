from rest_framework import serializers
from .models import Cliente
from backend.usuarios.serializers import backendUsuarioSerializer




class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Cliente
    """
    captado_por_info = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Cliente
        fields = [
            'id', 'rut', 'nombre', 'email', 'telefono', 'direccion',
            'captado_por', 'captado_por_info',
            # , 'fecha_captacion',
            #'estado', 'created_at', 'updated_at'
        ]
    def get_captado_por_info(self, obj):
        u = getattr(obj, 'captado_por', None)
        if u:
        # ajusta si quieres más datos
            return {'id': u.id, 'username': getattr(u, 'username', None)}
        return None
    
    def validate_rut(self, value):
        """
        Validar formato básico del RUT
        """
        if not value or len(value) < 9:
            raise serializers.ValidationError("RUT inválido")
        return value


class ClienteCreateSerializer(serializers.ModelSerializer):
    """
    Serializador para crear clientes (captación rápida)
    """
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'email', 'telefono', 'direccion', 'captado_por']
    
    def create(self, validated_data):
        # Estado por defecto ACTIVO
        validated_data['estado'] = 'ACTIVO'
        return super().create(validated_data)