import random
from datetime import date
from django.db import models
from django.utils import timezone
 
# Sin 0/O ni 1/I para que el código no se confunda al leerlo o dictarlo
ALFABETO = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
 
 
def generar_codigo():
    while True:
        codigo = "".join(random.choices(ALFABETO, k=6))
        if not Encomienda.objects.filter(codigo=codigo).exists():
            return codigo
 
 
class Encomienda(models.Model):
    codigo = models.CharField(max_length=8, editable=False, verbose_name="Código")
    descripcion = models.CharField(max_length=200)
    remitente = models.CharField(max_length=80)
    destinatario = models.CharField(max_length=80)
    fecha_registro = models.DateField(default=date.today)
 
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = generar_codigo()
        super().save(*args, **kwargs)
 
    def historial(self):
        return self.eventos.order_by("-hora")
 
    def ultimo_evento(self):
        return self.historial().first()
 
    def __str__(self):
        return f"{self.codigo}: {self.descripcion}"
 
 
class Punto(models.Model):
    nombre = models.CharField(max_length=60)
 
    class Meta:
        verbose_name = "Punto de control"
        verbose_name_plural = "Puntos de control"
 
    def __str__(self):
        return self.nombre
 
 
class Evento(models.Model):
    encomienda = models.ForeignKey(
        Encomienda, on_delete=models.CASCADE, related_name="eventos")
    punto = models.ForeignKey(
        Punto, on_delete=models.PROTECT, related_name="eventos")
    hora = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f"{self.encomienda.codigo} en {self.punto.nombre}"
