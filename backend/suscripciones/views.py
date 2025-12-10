from rest_framework import viewsets, permissions, status
from .models import Suscripcion, EventoSuscripcion
from .serializers import SuscripcionSerializer, EventoSuscripcionSerializer
from rest_framework.permissions import IsAuthenticated
from backend.usuarios.permissions import IsSoporteOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response




# =========================
#   SUSCRIPCIONES VIEWSET
# =========================
class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
    permission_classes = [IsAuthenticated, IsSoporteOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        cliente = self.request.query_params.get('cliente')
        estado = self.request.query_params.get('estado')
        if cliente:
            qs = qs.filter(cliente_id=cliente)
        if estado:
            qs = qs.filter(estado=estado)
        return qs
    
    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        """
        Cancela la suscripción y registra un evento de cambio de estado.
        """
        suscripcion = self.get_object()
        if suscripcion.estado == 'CANCELADA':
            return Response(
                {"detail": "La suscripción ya está cancelada."},
                status=status.HTTP_400_BAD_REQUEST
            )

        suscripcion.estado = 'CANCELADA'
        suscripcion.save()  # aquí se dispara la lógica de eventos en el modelo

        serializer = self.get_serializer(suscripcion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def cambiar_fecha(self, request, pk=None):
        """
        Cambia el día de cobro de la suscripción y actualiza proximo_cobro.
        """
        suscripcion = self.get_object()
        nuevo_dia = request.data.get("dia_cobro")

        try:
            nuevo_dia = int(nuevo_dia)
        except (TypeError, ValueError):
            return Response(
                {"detail": "dia_cobro debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not (1 <= nuevo_dia <= 28):
            return Response(
                {"detail": "dia_cobro debe estar entre 1 y 28."},
                status=status.HTTP_400_BAD_REQUEST
            )

        suscripcion.dia_cobro = nuevo_dia
        # Si tu modelo ya maneja proximo_cobro, puedes ajustar aquí.
        # Por ahora lo dejamos igual o lo recalculas según tu lógica.
        suscripcion.save()  # generará evento de tipo FECHA

        serializer = self.get_serializer(suscripcion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=True, methods=['post'])
    def cambiar_plan(self, request, pk=None):
        """
        Cambia el plan asociado a la suscripción, validando que el nuevo plan esté activo.
        """
        from planes.models import Plan  # import local para evitar ciclos

        suscripcion = self.get_object()
        nuevo_plan_id = request.data.get("plan")

        if not nuevo_plan_id:
            return Response(
                {"detail": "Debe enviar el ID del nuevo plan en el campo 'plan'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            nuevo_plan = Plan.objects.get(id=nuevo_plan_id, activo=True)
        except Plan.DoesNotExist:
            return Response(
                {"detail": "El plan indicado no existe o no está activo."},
                status=status.HTTP_400_BAD_REQUEST
            )

        suscripcion.plan = nuevo_plan
        suscripcion.monto_suscrito = nuevo_plan.monto  # opcional, si quieres sincronizar
        suscripcion.save()  # generará evento de tipo PLAN

        serializer = self.get_serializer(suscripcion)
        return Response(serializer.data, status=status.HTTP_200_OK)




# =========================
#   EVENTOS VIEWSET
# =========================
class EventoSuscripcionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventoSuscripcion.objects.all()
    serializer_class = EventoSuscripcionSerializer
    permission_classes = [IsAuthenticated, IsSoporteOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        suscripcion_id = self.request.query_params.get('suscripcion')
        tipo = self.request.query_params.get('tipo')
        if suscripcion_id:
            qs = qs.filter(suscripcion_id=suscripcion_id)
        if tipo:
            qs = qs.filter(tipo=tipo)
        return qs
