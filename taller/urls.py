from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.tablero, name="tablero"),
    path("seguimiento/", views.seguimiento_buscar, name="seguimiento_buscar"),
    path("seguimiento/<str:codigo>/", views.seguimiento, name="seguimiento"),
    path("escanear/<str:codigo>/", views.escanear, name="escanear"),
    path("qr/<str:codigo>.svg", views.qr, name="qr"),
    path("etiqueta/<str:codigo>/", views.etiqueta, name="etiqueta"),

]
