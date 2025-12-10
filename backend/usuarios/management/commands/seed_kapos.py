from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta

from backend.usuarios.models import Usuario
from backend.clientes.models import Cliente
from backend.planes.models import Plan
from backend.suscripciones.models import Suscripcion, EventoSuscripcion


class Command(BaseCommand):
    help = "Carga datos de ejemplo para demo/QA (Sprint 1)."

    def handle(self, *args, **options):
        # Usuario admin/soporte
        admin, _ = Usuario.objects.get_or_create(
            username="admin",
            defaults={"rol": "SOPORTE", "is_staff": True, "is_superuser": True},
        )
        if not admin.check_password("pass123"):
            admin.set_password("pass123")
            admin.save()
        self.stdout.write(self.style.SUCCESS(f"Usuario admin listo: {admin.username} / pass123"))

       # Clientes  (reemplaza este bloque)
        c1, _ = Cliente.objects.update_or_create(
            email="juan@example.com",
            defaults={
                "rut": "11.111.111-1",
                "nombre": "Juan",
                "telefono": "+56 9 1234 5678",
            },
        )

        c2, _ = Cliente.objects.update_or_create(
            email="maria@example.com",
            defaults={
                "rut": "22.222.222-2",
                "nombre": "María",
                "telefono": "+56 9 8765 4321",
            },
        )
        self.stdout.write(self.style.SUCCESS(f"Clientes OK: {c1.rut}, {c2.rut}"))

        # Planes
        p1, _ = Plan.objects.get_or_create(
            nombre="Mensual",
            defaults={
                "descripcion": "Plan mensual estándar",
                "monto": "4000.00",
                "periodicidad": "MENSUAL",
                "dia_cobro": 5,
                "activo": True,
            },
        )
        p2, _ = Plan.objects.get_or_create(
            nombre="Anual",
            defaults={
                "descripcion": "Plan anual preferente",
                "monto": "40000.00",
                "periodicidad": "ANUAL",
                "dia_cobro": 10,
                "activo": True,
            },
        )
        self.stdout.write(self.style.SUCCESS(f"Planes OK: {p1.nombre}, {p2.nombre}"))

        # Suscripción activa para c1 en p1
        hoy = date.today()
        prox = (hoy.replace(day=min(p1.dia_cobro, 28)) if hoy.day <= p1.dia_cobro
                else (hoy + timedelta(days=32)).replace(day=min(p1.dia_cobro, 28)))
        s1, created = Suscripcion.objects.get_or_create(
            cliente=c1, plan=p1, estado="ACTIVA",
            defaults={
                "fecha_inicio": hoy,
                "proximo_cobro": prox,
                "monto_suscrito": p1.monto,
                "dia_cobro": p1.dia_cobro,
            },
        )
        if created:
            EventoSuscripcion.objects.create(
                suscripcion=s1, tipo="CREADA",
                detalle="Suscripción creada por seed", actor=admin
            )
            EventoSuscripcion.objects.create(
                suscripcion=s1, tipo="ESTADO",
                detalle="Cambio de estado: PENDIENTE -> ACTIVA",
                metadata={"antes": "PENDIENTE", "despues": "ACTIVA"},
                actor=admin
            )
        self.stdout.write(self.style.SUCCESS(f"Suscripción OK: id={s1.id}, estado={s1.estado}"))

        self.stdout.write(self.style.SUCCESS("Seed KApos completado ✅"))
