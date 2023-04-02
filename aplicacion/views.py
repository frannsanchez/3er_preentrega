from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Usuario, Publicacion, Grupo

def mostrarUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "aplicacion/usuario.html", {"usuarios": usuarios})

def agregarUsuario(request):
    nombreU = request.GET.get("nombre")
    usuarioU = request.GET.get("usuario")
    contrasenaU = request.GET.get("contrasena")
    grupoU = request.GET.get("grupo")
    nuevoUsuario = Usuario(nombre=nombreU, usuario=usuarioU, contrasena=contrasenaU, grupo=grupoU)
    nuevoUsuario.save()
    
    return mostrarUsuarios(request)

def borrarUsuario(request, id):
    user = Usuario.objects.filter(id=id).first()
    user.delete()
    
    return mostrarUsuarios(request)

def buscarUsuario(request):
    criterio = request.GET.get("buscar")
    usuarios = Usuario.objects.filter(nombre__icontains=criterio).all()

    return render(request, "aplicacion/usuarioBuscar.html", {"usuarios": usuarios})

def editarUsuario(request, id): 
    user = Usuario.objects.filter(id=id).first()
    user.editar()
    user.save()
    return mostrarUsuarios(request)


