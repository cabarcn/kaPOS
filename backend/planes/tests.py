from rest_framework.test import APITestCase
from usuarios.models import Usuario

class PlanesCrudTests(APITestCase):
    def setUp(self):
        Usuario.objects.create_user(username='admin', password='pass123', rol='SOPORTE')
        r = self.client.post('/api/usuarios/login/', {"username":"admin","password":"pass123"}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {r.data['access']}")

    def test_crear_y_listar_activos(self):
        # Descubrir qué campos exige el POST
        meta = self.client.options('/api/planes/')
        print("OPTIONS status:", meta.status_code)
        print("OPTIONS actions:", meta.data.get('actions', {}))
        
        # CREATE
        r = self.client.post('/api/planes/', {
            "nombre": "Mensual",
            "descripcion": "Plan mensual estándar",
            "monto": "4000.00",
            "periodicidad": "MENSUAL",
            "dia_cobro": 5,
            "activo": True
        }, format='json')
        
        print("CREATE status:", r.status_code)
        try:
            print("CREATE data:", r.data)
        except Exception as e:
            print('CREATE data (error al leer .data):', e)
        print("RAW:", getattr(r, "content", b"").decode(errors="ignore"))
                
        # diagnóstico
        print("CREATE status:", r.status_code)
        print("CREATE data:", r.data)
        
        assert r.status_code in (201, 200)

        # ACTIVOS
        r = self.client.get('/api/planes/activos/')
        assert r.status_code == 200
        assert any(p.get('nombre') == 'Mensual' for p in r.data)

