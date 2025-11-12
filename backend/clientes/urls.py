from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

# Router para el ViewSet (crea automáticamente todas las rutas CRUD)
router = DefaultRouter()
router.register(r'', ClienteViewSet, basename='cliente')

urlpatterns = [
    path('', include(router.urls)),
]