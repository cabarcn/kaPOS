from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Planes
    """
    
    # Campos que se muestran en la lista
    list_display = ['nombre', 'monto', 'periodicidad', 'dia_cobro', 'activo', 'created_at']
    
    # Filtros en el sidebar
    list_filter = ['periodicidad', 'activo', 'created_at']
    
    # Búsqueda
    search_fields = ['nombre', 'descripcion']
    
    # Campos editables desde la lista
    list_editable = ['activo']
    
    # Campos de solo lectura
    readonly_fields = ['created_at', 'updated_at']
    
    # Organización del formulario
    fieldsets = (
        ('Información del Plan', {
            'fields': ('nombre', 'descripcion', 'monto', 'periodicidad')
        }),
        ('Configuración', {
            'fields': ('dia_cobro', 'activo')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )