from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Usuario, Publicacion, Grupo

def mostrarUsuarios(request):
    usuario = Usuario.objets.all()
    return render({request, "aplicacion/usuario.html", {"usuarios": usuario}})

