from django.contrib.auth.models import AbstractUser
from django.db import models
from backend.usuarios.models import Usuario


class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que extiende el usuario de Django
    """
    
    # Roles disponibles en el sistema
    ROLES = [
        ('INVITADO', 'Invitado'),
        ('CLIENTE', 'Cliente'),
        ('CAPTADOR', 'Captador'),
        ('COORDINADOR_CAPTADORES', 'Coordinador de Captadores'),
        ('COORDINADOR_GENERAL', 'Coordinador General'),
        ('ENCARGADO_AREA', 'Encargado de Área'),
        ('SOPORTE', 'Soporte'),
    ]
    
    # Campos adicionales
    rol = models.CharField(
        max_length=30,
        choices=ROLES,
        default='INVITADO',
        help_text='Rol del usuario en el sistema'
    )
    
    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='Teléfono de contacto'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha de creación'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Fecha de última actualización'
    )
    
   
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuario_set',  # Cambiado
        related_query_name='usuario',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuario_set',  # Cambiado
        related_query_name='usuario',
    )
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
    
   