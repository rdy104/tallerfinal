from django.contrib import admin
from .models import Mecanico, Vehiculo, Orden
 
 
@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ("vehiculo", "descripcion", "mecanico", "estado", "fecha_ingreso")
    list_filter = ("estado", "mecanico")
 
 
admin.site.register(Mecanico)
admin.site.register(Vehiculo)
