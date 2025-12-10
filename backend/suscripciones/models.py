from django.db import models
from backend.clientes.models import Cliente
from backend.planes.models import Plan
from django.utils import timezone
from django.conf import settings

class Suscripcion(models.Model):
    """
    Modelo de Suscripción - Vincula Cliente con Plan
    """

    # Relaciones
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='suscripciones',
        help_text='Cliente suscrito'
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name='suscripciones',
        help_text='Plan contratado'
    )

    # Estados de suscripción
    ESTADOS = [
        ('PENDIENTE', 'Pendiente de Activación'),
        ('ACTIVA', 'Activa'),
        ('PAUSADA', 'Pausada'),
        ('CANCELADA', 'Cancelada'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='PENDIENTE',
        help_text='Estado actual de la suscripción'
    )

    # Fechas
    fecha_inicio = models.DateField(
        help_text='Fecha de inicio de la suscripción'
    )
    fecha_fin = models.DateField(
        blank=True,
        null=True,
        help_text='Fecha de finalización (si fue cancelada)'
    )
    proximo_cobro = models.DateField(
        help_text='Fecha del próximo cobro programado'
    )
    dia_cobro = models.IntegerField(
        help_text='Día del mes para realizar el cobro'
    )

    # Monto (guardado al momento de suscribirse)
    monto_suscrito = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Monto al que se suscribió (puede diferir del plan actual)'
    )

    # Motivo de cancelación
    motivo_cancelacion = models.TextField(
        blank=True,
        null=True,
        help_text='Motivo de cancelación o pausa'
    )

    # Auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Suscripción'
        verbose_name_plural = 'Suscripciones'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.cliente.nombre} - {self.plan.nombre} ({self.get_estado_display()})"

    def save(self, *args, **kwargs):
        """
        Guardado con bitácora de eventos automáticos.
        """
        from .models import EventoSuscripcion  # import local para evitar ciclos
        cambios = {}

        if self.pk:
            anterior = Suscripcion.objects.get(pk=self.pk)
            if anterior.estado != self.estado:
                cambios['estado'] = {'antes': anterior.estado, 'despues': self.estado}
            if anterior.plan_id != self.plan_id:
                cambios['plan'] = {'antes': anterior.plan_id, 'despues': self.plan_id}
            if (
                anterior.dia_cobro != self.dia_cobro or
                anterior.proximo_cobro != self.proximo_cobro or
                anterior.fecha_inicio != self.fecha_inicio
            ):
                cambios['fecha'] = {
                    'dia_cobro': {'antes': anterior.dia_cobro, 'despues': self.dia_cobro},
                    'proximo_cobro': {'antes': str(anterior.proximo_cobro), 'despues': str(self.proximo_cobro)},
                    'fecha_inicio': {'antes': str(anterior.fecha_inicio), 'despues': str(self.fecha_inicio)},
                }
        else:
            cambios['creada'] = True
            # Solo en creación: establecer monto y día desde plan
            self.monto_suscrito = self.plan.monto
            self.dia_cobro = self.plan.dia_cobro

        super().save(*args, **kwargs)

        # Registrar eventos una vez guardado
        if 'creada' in cambios:
            EventoSuscripcion.objects.create(
                suscripcion=self,
                tipo='CREADA',
                detalle='Suscripción creada',
                metadata=None
            )

        if 'estado' in cambios:
            EventoSuscripcion.objects.create(
                suscripcion=self,
                tipo='ESTADO',
                detalle=f"Cambio de estado: {cambios['estado']['antes']} -> {cambios['estado']['despues']}",
                metadata=cambios['estado']
            )

        if 'plan' in cambios:
            EventoSuscripcion.objects.create(
                suscripcion=self,
                tipo='PLAN',
                detalle=f"Cambio de plan: {cambios['plan']['antes']} -> {cambios['plan']['despues']}",
                metadata=cambios['plan']
            )

        if 'fecha' in cambios:
            EventoSuscripcion.objects.create(
                suscripcion=self,
                tipo='FECHA',
                detalle="Actualización de fecha/día/proximo_cobro",
                metadata=cambios['fecha']
            )


class EventoSuscripcion(models.Model):
    TIPOS = [
        ('CREADA', 'Creada'),
        ('ESTADO', 'Cambio de estado'),
        ('PLAN', 'Cambio de plan'),
        ('FECHA', 'Cambio de fecha/día/proximo_cobro'),
        ('MANDATO', 'Validación de mandato'),
        ('OTRO', 'Otro'),
    ]

    suscripcion = models.ForeignKey(
        'Suscripcion',
        on_delete=models.CASCADE,
        related_name='eventos'
    )
    tipo = models.CharField(max_length=20, choices=TIPOS)
    detalle = models.TextField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='eventos_realizados'
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.suscripcion_id} - {self.tipo} - {self.created_at:%Y-%m-%d %H:%M}'
