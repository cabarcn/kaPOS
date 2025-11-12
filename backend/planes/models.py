from django.db import models

class Plan(models.Model):
    """
    Modelo de Plan de Donación
    Define los planes mensuales, trimestrales y anuales
    """
    
    # Periodicidad del plan
    PERIODICIDAD_CHOICES = [
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('ANUAL', 'Anual'),
    ]
    
    nombre = models.CharField(
        max_length=100,
        help_text='Nombre del plan (ej: Plan Básico Mensual)'
    )
    
    descripcion = models.TextField(
        blank=True,
        null=True,
        help_text='Descripción del plan'
    )
    
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Monto de la donación'
    )
    
    periodicidad = models.CharField(
        max_length=20,
        choices=PERIODICIDAD_CHOICES,
        help_text='Periodicidad del plan'
    )
    
    # Estado del plan
    activo = models.BooleanField(
        default=True,
        help_text='Si el plan está disponible para captación'
    )
    
    # Configuración de cobro
    dia_cobro = models.IntegerField(
        default=5,
        help_text='Día del mes para realizar el cobro (1-28)'
    )
    
    # Auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        ordering = ['periodicidad', 'monto']
    
    def __str__(self):
        return f"{self.nombre} - ${self.monto} ({self.get_periodicidad_display()})"
    
    def clean(self):
        """
        Validaciones personalizadas
        """
        from django.core.exceptions import ValidationError
        
        if self.dia_cobro < 1 or self.dia_cobro > 28:
            raise ValidationError('El día de cobro debe estar entre 1 y 28')
        
        if self.monto <= 0:
            raise ValidationError('El monto debe ser mayor a 0')