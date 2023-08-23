from django.urls import path
from .views import *
from AppCoder import views

urlpatterns = [  
    path("crear_medicos/", crear_medicos),
    path("listar_medicos/", listar_medicos),
    path("medicos/", medicos, name="Medicos"),
    path("hospitales/", hospitales, name= "Hospitales"), 
    path("obra_social/", obrasocial, name= "Obra Social"),
    path ("busquedaMedicos/", busquedaMedicos , name= "busquedaMedicos"),
    path("buscar", views.buscar, name="buscar"),

]
