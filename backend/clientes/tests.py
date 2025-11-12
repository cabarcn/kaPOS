from rest_framework.test import APITestCase
from usuarios.models import Usuario

class ClientesCrudTests(APITestCase):
    def setUp(self):
        Usuario.objects.create_user(username='admin', password='pass123', rol='SOPORTE')
        # login para obtener token
        r = self.client.post('/api/usuarios/login/', {"username": "admin", "password": "pass123"}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {r.data['access']}")

    def test_crud_cliente(self):
        # CREATE
        payload = {
            "nombre": "Juan",
            "rut": "11.111.111-1",
            "email": "juan@example.com",
            "telefono": "+56 9 1234 5678"
        }
        r = self.client.post('/api/clientes/', payload, format='json')
        print("CREATE status:", r.status_code)
        print("CREATE data:", r.data)
        assert r.status_code in (201, 200)
        #cid = r.data['id']

        # LIST
        r_list = self.client.get('/api/clientes/')
        assert r_list.status_code == 200
        cid = None
        for c in r_list.data:
            if c.get('email') == "juan@example.com":
                cid = c.get('id')
                break
        assert cid is not None, "no se encontró el cliente recien creado en el listado"

        # DETAIL
        r = self.client.get(f'/api/clientes/{cid}/')
        assert r.status_code == 200
        assert r.data['email'] == "juan@example.com"

        # UPDATE (PATCH)
        r = self.client.patch(f'/api/clientes/{cid}/', {"telefono": "+56 9 0000 0000"}, format='json')
        assert r.status_code in (200, 202)
