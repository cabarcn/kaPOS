from rest_framework import viewsets, permissions
from .models import Suscripcion, EventoSuscripcion
from .serializers import SuscripcionSerializer, EventoSuscripcionSerializer


# =========================
#   SUSCRIPCIONES VIEWSET
# =========================
class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all().order_by('-created_at')
    serializer_class = SuscripcionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        cliente = self.request.query_params.get('cliente')
        estado = self.request.query_params.get('estado')
        if cliente:
            qs = qs.filter(cliente_id=cliente)
        if estado:
            qs = qs.filter(estado=estado)
        return qs


# =========================
#   EVENTOS VIEWSET
# =========================
class EventoSuscripcionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventoSuscripcion.objects.select_related('suscripcion').all()
    serializer_class = EventoSuscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        suscripcion_id = self.request.query_params.get('suscripcion')
        tipo = self.request.query_params.get('tipo')
        if suscripcion_id:
            qs = qs.filter(suscripcion_id=suscripcion_id)
        if tipo:
            qs = qs.filter(tipo=tipo)
        return qs
