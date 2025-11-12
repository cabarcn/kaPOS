from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """
    Configuración del panel de administración para Usuarios
    """
    
    # Campos que se muestran en la lista
    list_display = ['username', 'email', 'rol', 'first_name', 'last_name', 'is_active', 'created_at']
    
    # Filtros en el sidebar
    list_filter = ['rol', 'is_active', 'is_staff', 'created_at']
    
    # Búsqueda
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    # Agregar campos personalizados al formulario
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {
            'fields': ('rol', 'telefono')
        }),
    )
    
    # Campos para crear usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {
            'fields': ('rol', 'telefono', 'email')
        }),
    )