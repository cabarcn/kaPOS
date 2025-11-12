from django.contrib import admin
from .models import Suscripcion

@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Suscripciones
    """
    
    # Campos que se muestran en la lista
    list_display = [
        'id', 'cliente', 'plan', 'estado', 
        'monto_suscrito', 'fecha_inicio', 'proximo_cobro'
    ]
    
    # Filtros en el sidebar
    list_filter = ['estado', 'fecha_inicio', 'plan__periodicidad']
    
    # Búsqueda
    search_fields = ['cliente__nombre', 'cliente__rut', 'plan__nombre']
    
    # Campos de solo lectura
    readonly_fields = ['created_at', 'updated_at', 'monto_suscrito']
    
    # Organización del formulario
    fieldsets = (
        ('Información de Suscripción', {
            'fields': ('cliente', 'plan', 'estado')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin', 'proximo_cobro', 'dia_cobro')
        }),
        ('Montos', {
            'fields': ('monto_suscrito',)
        }),
        ('Cancelación', {
            'fields': ('motivo_cancelacion',),
            'classes': ('collapse',)
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        """
        Si la suscripción ya existe, no permitir cambiar cliente ni plan
        """
        if obj:  # Editando
            return self.readonly_fields + ['cliente', 'plan']
        return self.readonly_fields