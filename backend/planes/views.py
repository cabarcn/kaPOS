from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Plan
from .serializers import PlanSerializer, PlanListSerializer

class PlanViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Planes
    
    list: Listar todos los planes
    create: Crear nuevo plan (solo coordinadores/encargados)
    retrieve: Ver detalle de un plan
    update: Actualizar plan completo
    partial_update: Actualizar plan parcialmente
    destroy: Eliminar plan
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    
    def get_permissions(self):
        """
        Permisos según la acción
        """
        if self.action in ['list', 'retrieve', 'activos']:
            # Cualquiera autenticado puede ver planes
            return [IsAuthenticated()]
        else:
            # Solo coordinadores y encargados pueden crear/editar/eliminar
            return [IsAuthenticated()]
    
    def get_queryset(self):
        """
        Filtrar planes según parámetros
        """
        queryset = Plan.objects.all()
        
        # Filtro por periodicidad
        periodicidad = self.request.query_params.get('periodicidad', None)
        if periodicidad:
            queryset = queryset.filter(periodicidad=periodicidad)
        
        # Filtro por activo
        activo = self.request.query_params.get('activo', None)
        if activo is not None:
            queryset = queryset.filter(activo=activo.lower() == 'true')
        
        return queryset
    
    def get_serializer_class(self):
        """
        Usar serializador simplificado para listar
        """
        if self.action == 'list':
            return PlanListSerializer
        return PlanSerializer
    
    @action(detail=False, methods=['get'])
    def activos(self, request):
        """
        Listar solo planes activos (para captación)
        GET /api/planes/activos/
        """
        planes = Plan.objects.filter(activo=True)
        serializer = PlanListSerializer(planes, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def activar(self, request, pk=None):
        """
        Activar un plan
        POST /api/planes/{id}/activar/
        """
        plan = self.get_object()
        plan.activo = True
        plan.save()
        return Response({
            'message': 'Plan activado exitosamente',
            'plan': PlanSerializer(plan).data
        })
    
    @action(detail=True, methods=['post'])
    def desactivar(self, request, pk=None):
        """
        Desactivar un plan
        POST /api/planes/{id}/desactivar/
        """
        plan = self.get_object()
        plan.activo = False
        plan.save()
        return Response({
            'message': 'Plan desactivado exitosamente',
            'plan': PlanSerializer(plan).data
        })