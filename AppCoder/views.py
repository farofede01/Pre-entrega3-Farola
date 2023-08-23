from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from .forms import medicoForm, hospitalForm, obrasocialForm
# Create your views here.

def inicio (request):
    return render (request, "AppCoder/inicio.html")

def hospitales(request):
    if request.method == "POST":
        form = hospitalForm(request.POST)
        if form.is_valid ():
            info = form.cleaned_data
            nombre = info ["nombre"]
            num_telefono = info ["num_telefono"]
            direccion = info ["direccion"]
            email = ["email"]
            hospital = Hospitales(nombre = nombre, num_telefono = num_telefono, direccion = direccion, email = email)
            hospital.save()
            formulario_hospital = hospitalForm()
            return render (request, "AppCoder/hospitales.html", {"mensaje":"Hospital creado"})
        else:
            return render (request, "AppCoder/hospitales.html", {"mensaje": "Datos invalidos"})
    else:   
        formulario_hospital = hospitalForm()
    
    return render(request, "AppCoder/hospitales.html", {"formulario": formulario_hospital})
    
 
def crear_medicos(request):
    nombre_medico = "Fede Farola"
    dni_medico = 39985288
    email_medico = "fede@farola.com"
    print("Creando Medicos")
    medico = Medicos(nombre=nombre_medico, dni=dni_medico, email=email_medico)
    medico.save()
    respuesta = f"Medico creado: {nombre_medico} - {dni_medico} - {email_medico}"
    return HttpResponse(respuesta)

def listar_medicos(request):
    medicos = Medicos.objects.all()
    respuesta = ""
    for medico in medicos:
        respuesta += f"{medico.nombre} - {medico.dni} - {medico.email}\n"
    return HttpResponse(respuesta)

def medicos(request):
    if request.method == "POST":
        form = medicoForm(request.POST)
        if form.is_valid ():
            info = form.cleaned_data
            nombre = info ["nombre"]
            dni = info ["dni"]
            email = ["email"]
            medico = Medicos(nombre = nombre, dni = dni, email = email)
            medico.save ()
            formulario_medico = medicoForm ()
            return render(request,"AppCoder/medicos.html", {"mensaje " : "Medico creado"})
        return render(request,"AppCoder/medicos.html", {"mensaje " : "Datos invalidos"})
    else:
        formulario_medico = medicoForm()
        return render (request,"AppCoder/medicos.html",{"formulario": formulario_medico})
   
def obrasocial (request):
    if request.method == "POST":
        form = obrasocialForm(request.POST)
        if form.is_valid ():
            info = form.cleaned_data
            nombre = info ["nombre"]
            email = ["email"]
            obrasocial = Obrasocial(nombre = nombre, email = email)
            obrasocial.save ()
            mensaje = "Obra Social creada"
        else :
            mensaje = "Datos invalidos"
    else :
        mensaje = ""
    formulario_obrasocial = obrasocialForm()
    hospitales = Hospitales.objects.all ()
    return render ( request, "AppCoder/ObraSocial.html", {"mensaje": mensaje, "formulario": formulario_obrasocial, "hospitales": hospitales})

def busquedaMedicos(request):
    return render (request, "AppCoder/busquedaMedicos.html")

def buscar (request):
    nombre = request.GET["nombre"]
    if nombre!= "":
        medico= Medicos.objects.filter(nombre__icontains = nombre)
        return render( request, "AppCoder/resultadosBusqueda.html", {"medicos" :medico})
    else:
        return render(request, "AppCoder/busquedaMedicos.html", {"mensaje":"No se ingresó nada"})
    
