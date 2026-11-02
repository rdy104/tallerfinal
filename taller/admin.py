from django.contrib import admin
from .models import Encomienda, Punto, Evento
 
 
@admin.register(Encomienda)
class EncomiendaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descripcion", "remitente", "destinatario", "fecha_registro")
    readonly_fields = ("codigo",)
 
 
admin.site.register(Punto)
 
 
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("encomienda", "punto", "hora")
    list_filter = ("punto",)
