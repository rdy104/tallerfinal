import io
 
import segno
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
 
from .models import Encomienda, Punto, Evento

from .models import Encomienda, Punto, Evento
 
 
def tablero(request):
    lista = Encomienda.objects.order_by("fecha_registro", "pk")
    return render(request, "taller/tablero.html", {"encomiendas": lista})
 
 
def seguimiento_buscar(request):
    codigo = request.GET.get("codigo", "").strip().upper()
    if codigo:
        return redirect("seguimiento", codigo=codigo)
    return render(request, "taller/seguimiento_buscar.html")
 
 
def seguimiento(request, codigo):
    encomienda = Encomienda.objects.filter(codigo=codigo.upper()).first()
    contexto = {"encomienda": encomienda, "codigo": codigo.upper()}
    estado = 200 if encomienda else 404
    return render(request, "taller/seguimiento.html", contexto, status=estado)

def escanear(request, codigo):
    encomienda = Encomienda.objects.filter(codigo=codigo.upper()).first()
    if encomienda is None:
        return render(request, "taller/escanear.html",
                      {"codigo": codigo.upper()}, status=404)
    if request.method == "POST":
        punto = Punto.objects.filter(pk=request.POST.get("punto")).first()
        if punto:
            Evento.objects.create(encomienda=encomienda, punto=punto)
        return redirect("escanear", codigo=encomienda.codigo)
    contexto = {"encomienda": encomienda, "codigo": encomienda.codigo,
                "puntos": Punto.objects.all()}
    return render(request, "taller/escanear.html", contexto)

def qr(request, codigo):
    direccion = request.build_absolute_uri(reverse("escanear", args=[codigo]))
    imagen = segno.make(direccion)
    salida = io.BytesIO()
    imagen.save(salida, kind="svg", scale=6)
    return HttpResponse(salida.getvalue(), content_type="image/svg+xml")
 
 
def etiqueta(request, codigo):
    encomienda = get_object_or_404(Encomienda, codigo=codigo.upper())
    return render(request, "taller/etiqueta.html", {"encomienda": encomienda})
