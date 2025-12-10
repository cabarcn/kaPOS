from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('backend.usuarios.urls')),
    path('api/clientes/', include('backend.clientes.urls')),
    path('api/planes/', include('backend.planes.urls')),
    path('api/suscripciones/', include('backend.suscripciones.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   
]