from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.ordenes, name="ordenes"),
    path("vehiculos/<int:pk>/", views.ficha, name="ficha"),
]
