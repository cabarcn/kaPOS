from rest_framework.test import APITestCase
from backend.usuarios.models import Usuario

class AuthTests(APITestCase):
    def setUp(self):
        Usuario.objects.create_user(username='tester', password='pass123', rol='CLIENTE')

    def test_login_ok(self):
        r = self.client.post('/api/usuarios/login/', {
            "username": "tester",
            "password": "pass123"
        }, format='json')
        assert r.status_code == 200
        assert 'access' in r.data
