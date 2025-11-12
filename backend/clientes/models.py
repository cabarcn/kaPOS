from django.db import models
from usuarios.models import Usuario

class Cliente(models.Model):
    """
    Modelo de Cliente/Socio - Personas que donan
    """
    
    # Información personal
    rut = models.CharField(
        max_length=12,
        unique=True,
        help_text='RUT del cliente (ej: 12345678-9)'
    )
    
    nombre = models.CharField(
        max_length=100,
        help_text='Nombre completo del cliente'
    )
    
    email = models.EmailField(
        unique=True,
        help_text='Email del cliente'
    )
    
    telefono = models.CharField(
        max_length=20,
        help_text='Teléfono de contacto'
    )
    
    direccion = models.TextField(
        blank=True,
        null=True,
        help_text='Dirección del cliente'
    )
    
    # Información de captación
    captado_por = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clientes_captados',
        limit_choices_to={'rol': 'CAPTADOR'},
        help_text='Captador que inscribió al cliente'
    )
    
    fecha_captacion = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha en que se captó al cliente'
    )
    
    # Estado
    ESTADOS = [
        ('ACTIVO', 'Activo'),
        ('PAUSADO', 'Pausado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='ACTIVO',
        help_text='Estado actual del cliente'
    )
    
    # Auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.nombre} ({self.rut})"