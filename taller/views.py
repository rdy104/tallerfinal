from django.shortcuts import render, get_object_or_404
from .models import Mecanico, Vehiculo, Orden
 
 
def ordenes(request):
    mecanico_id = request.GET.get("mecanico")
    lista = Orden.objects.exclude(estado="Entregado").order_by("fecha_ingreso")
    if mecanico_id:
        lista = lista.filter(mecanico_id=mecanico_id)
    contexto = {"ordenes": lista, "mecanicos": Mecanico.objects.all()}
    return render(request, "taller/ordenes.html", contexto)
 
 
def ficha(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    historial = vehiculo.ordenes.order_by("-fecha_ingreso")
    contexto = {"vehiculo": vehiculo, "historial": historial}
    return render(request, "taller/ficha.html", contexto)
