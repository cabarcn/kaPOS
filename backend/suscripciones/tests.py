from rest_framework.test import APITestCase
from django.utils import timezone
from backend.usuarios.models import Usuario
from clientes.models import Cliente
from planes.models import Plan

class SuscripcionesFlowTests(APITestCase):
    def setUp(self):
        # usuario y token
        Usuario.objects.create_user(username='admin', password='pass123', rol='SOPORTE')
        r = self.client.post('/api/usuarios/login/', {"username":"admin","password":"pass123"}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {r.data['access']}")

        # datos base
        self.cliente = Cliente.objects.create(
            rut='22.222.222-2', nombre='Ana', email='ana@example.com', telefono='+56911111111'
        )
        self.plan = Plan.objects.create(
            nombre='Mensual', monto='4000.00', periodicidad='MENSUAL', dia_cobro=5, activo=True
        )

    def test_crea_suscripcion_y_registra_eventos(self):
        hoy = timezone.now().date().isoformat()

        # CREATE suscripción
        r = self.client.post('/api/suscripciones/', {
            "cliente": self.cliente.id,
            "plan": self.plan.id,
            "estado": "PENDIENTE",
            "fecha_inicio": hoy,
            "proximo_cobro": hoy,
            "dia_cobro": 5,
            "monto_suscrito": "4000.00"
        }, format='json')
        assert r.status_code in (201, 200)
        sid = r.data.get('id') or self.client.get('/api/suscripciones/').data[0]['id']

        # Debe existir evento CREADA
        ev = self.client.get(f'/api/suscripciones/eventos/?suscripcion={sid}')
        assert ev.status_code == 200
        assert any(e.get('tipo') == 'CREADA' for e in ev.data)

        # Cambiar estado → debe crear evento ESTADO
        r = self.client.patch(f'/api/suscripciones/{sid}/', {"estado": "ACTIVA"}, format='json')
        assert r.status_code in (200, 202)

        ev2 = self.client.get(f'/api/suscripciones/eventos/?suscripcion={sid}')
        assert ev2.status_code == 200
        assert any(e.get('tipo') == 'ESTADO' for e in ev2.data)
