from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Usuario
    Convierte objetos Usuario a JSON y viceversa
    """
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rol', 'telefono', 'created_at']
        read_only_fields = ['id', 'created_at']


class RegistroSerializer(serializers.ModelSerializer):
    """
    Serializador para registro de nuevos usuarios
    """
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, label="Confirmar contraseña")
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'telefono', 'rol']
    
    def validate(self, data):
        """
        Validar que las contraseñas coincidan
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data
    
    def create(self, validated_data):
        """
        Crear nuevo usuario con contraseña encriptada
        """
        validated_data.pop('password2')  # Remover password2
        password = validated_data.pop('password')
        
        usuario = Usuario(**validated_data)
        usuario.set_password(password)  # Encriptar contraseña
        usuario.save()
        
        return usuario
    
class backendUsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer usado por las vistas del backend para exponer datos de Usuario.
    Es equivalente a un UsuarioSerializer general.
    """

    class Meta:
        model = Usuario
        fields = "__all__"
