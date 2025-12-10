from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Cliente
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from backend.usuarios.permissions import IsSoporteOrReadOnly
from .serializers import ClienteSerializer, ClienteCreateSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Clientes
    
    list: Listar todos los clientes
    create: Crear nuevo cliente
    retrieve: Ver detalle de un cliente
    update: Actualizar cliente completo
    partial_update: Actualizar cliente parcialmente
    destroy: Eliminar cliente
    """
    queryset = Cliente.objects.all().order_by('-id')
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, IsSoporteOrReadOnly]
    
    # 👇 NUEVO: forzar respuesta con serializer de lectura (incluye id)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        read_serializer = self.get_serializer(serializer.instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)
    
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ClienteCreateSerializer
        return ClienteSerializer
    
    def get_queryset(self):
        """
        Filtrar clientes según rol del usuario
        """
        user = self.request.user
        queryset = Cliente.objects.all()
        
        # Si es captador, solo ve sus clientes
        if user.rol == 'CAPTADOR':
            queryset = queryset.filter(captado_por=user)
        
        # Filtros por query params
        estado = self.request.query_params.get('estado', None)
        if estado:
            queryset = queryset.filter(estado=estado)
        
        return queryset.select_related('captado_por')
    
    @action(detail=True, methods=['post'])
    def pausar(self, request, pk=None):
        """
        Pausar suscripción del cliente
        POST /api/clientes/{id}/pausar/
        """
        cliente = self.get_object()
        cliente.estado = 'PAUSADO'
        cliente.save()
        return Response({
            'message': 'Cliente pausado exitosamente',
            'cliente': ClienteSerializer(cliente).data
        })
    
    @action(detail=True, methods=['post'])
    def activar(self, request, pk=None):
        """
        Activar cliente
        POST /api/clientes/{id}/activar/
        """
        cliente = self.get_object()
        cliente.estado = 'ACTIVO'
        cliente.save()
        return Response({
            'message': 'Cliente activado exitosamente',
            'cliente': ClienteSerializer(cliente).data
        })
    
    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        """
        Cancelar suscripción del cliente
        POST /api/clientes/{id}/cancelar/
        """
        cliente = self.get_object()
        cliente.estado = 'CANCELADO'
        cliente.save()
        return Response({
            'message': 'Cliente cancelado exitosamente',
            'cliente': ClienteSerializer(cliente).data
        })