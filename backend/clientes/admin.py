from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Clientes
    """
    
    # Campos que se muestran en la lista
    list_display = ['rut', 'nombre', 'email', 'telefono', 'estado', 'captado_por', 'fecha_captacion']
    
    # Filtros en el sidebar
    list_filter = ['estado', 'fecha_captacion', 'captado_por']
    
    # Búsqueda
    search_fields = ['rut', 'nombre', 'email', 'telefono']
    
    # Campos de solo lectura
    readonly_fields = ['fecha_captacion', 'created_at', 'updated_at']
    
    # Organización del formulario
    fieldsets = (
        ('Información Personal', {
            'fields': ('rut', 'nombre', 'email', 'telefono', 'direccion')
        }),
        ('Información de Captación', {
            'fields': ('captado_por', 'fecha_captacion', 'estado')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )