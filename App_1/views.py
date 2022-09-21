from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Usuario
# Create your views here.

def padre(request):
    return render(request, "App_1/padre.html")

def inicio(request):
    return render(request, "App_1/inicio.html")

def formulario1(request):

    if request.method=="POST":

        formulario1 = CrearUsuario(request.POST)
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            UserF = Usuario(user = info["user"], contraseña = info["contraseña"], email = info["email"], telefono = ["numero"])

            UserF.save()

            return render(request, "App_1/inicio.html")

    else:
        formulario1 = ()

    return render(request, "App_1/formulario1.html", {"form1":formulario1})