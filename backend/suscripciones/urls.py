from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuscripcionViewSet, EventoSuscripcionViewSet

router = DefaultRouter()
router.register(r'eventos', EventoSuscripcionViewSet, basename='evento-suscripcion')
router.register(r'', SuscripcionViewSet, basename='suscripcion')


urlpatterns = [
    path('', include(router.urls)),
]
