from django.db import models

# Create your models here.
from datetime import date
from django.db import models
 
 
class Mecanico(models.Model):
    nombre = models.CharField(max_length=80)
    especialidad = models.CharField(max_length=80)
 
    class Meta:
        verbose_name = "Mecánico"
        verbose_name_plural = "Mecánicos"
 
    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"
 
 
class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name="Año")
    propietario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
 
    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
 
    def __str__(self):
        return f"{self.placa} — {self.marca} {self.modelo}"
 
 
class Orden(models.Model):
    ESTADOS = [
        ("Recibido", "Recibido"),
        ("En reparación", "En reparación"),
        ("Listo", "Listo"),
        ("Entregado", "Entregado"),
    ]
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, related_name="ordenes")
    mecanico = models.ForeignKey(
        Mecanico, on_delete=models.PROTECT, related_name="ordenes")
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="Recibido")
    fecha_ingreso = models.DateField(default=date.today)
 
    class Meta:
        verbose_name_plural = "Órdenes"
 
    def __str__(self):
        return f"{self.vehiculo.placa}: {self.descripcion}"
