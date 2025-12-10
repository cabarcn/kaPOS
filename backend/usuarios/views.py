from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Usuario
from .serializers import UsuarioSerializer, RegistroSerializer


class RegistroView(generics.CreateAPIView):
    """
    Endpoint para registro de nuevos usuarios
    POST /api/usuarios/registro/
    """
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]  # Cualquiera puede registrarse
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        
        return Response({
            'message': 'Usuario creado exitosamente',
            'usuario': UsuarioSerializer(usuario).data
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """
    Endpoint para login (autenticación)
    POST /api/usuarios/login/
    Body: { "username": "...", "password": "..." }
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        print(f"=== DEBUG LOGIN ===")
        print(f"Username recibido: '{username}'")
        print(f"Password recibido: '{password}'")
        
        if not username or not password:
            return Response({
                'error': 'Por favor proporciona username y password'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Autenticar usuario
        usuario = authenticate(request=request, username=username, password=password)
        print(f"Usuario autenticado: {usuario}")
        
        if usuario is None:
            return Response({
                'error': 'Credenciales inválidas'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        if not usuario.is_active:
            return Response({
                'error': 'Usuario inactivo'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        # Generar tokens JWT
        refresh = RefreshToken.for_user(usuario)
        
        return Response({
            'message': 'Login exitoso',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'usuario': UsuarioSerializer(usuario).data
        }, status=status.HTTP_200_OK)


class PerfilView(APIView):
    """
    Endpoint para obtener perfil del usuario autenticado
    GET /api/usuarios/perfil/
    Requiere token JWT en header: Authorization: Bearer <token>
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)