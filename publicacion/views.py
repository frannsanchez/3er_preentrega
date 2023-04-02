from django.shortcuts import render
from django.http import HttpResponse
from publicacion.models import Publicacion

def mostrarPublicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "publicacion/publicacion.html", {"publicaciones": publicaciones})

def agregarPublicacion(request):
    usuarioU = request.GET.get("usuario")
    tituloU = request.GET.get("titulo")
    cuerpoU = request.GET.get("cuerpo")
    nuevaPublicacion = Publicacion(usuario=usuarioU, titulo=tituloU, cuerpo=cuerpoU)
    nuevaPublicacion.save()
    return mostrarPublicaciones(request)

def borrarPublicacion(request, id):
    publicacion = Publicacion.objects.filter(id=id).first()
    publicacion.delete()
    return mostrarPublicaciones(request)

def buscarPublicacion(request):
    criterio = request.GET.get("buscar")
    if criterio:
        publicaciones = Publicacion.objects.filter(usuario__icontains=criterio).all()
        return render(request, "publicacion/publicacionBuscar.html", {"publicaciones":publicaciones})
    return render(request, "publicacion/publicacionBuscar.html")


def editarPublicacion(request, id): 
    publicacion = Publicacion.objects.filter(id=id).first()
    if request.method == 'POST':
        variable = request.POST.get('variable')
        nuevo = request.POST.get('nuevo')
        publicacion.editar(variable, nuevo)
        publicacion.save()
        return mostrarPublicaciones(request)
    return render(request, 'publicacion/publicacionEditar.html', {'publicacion': publicacion})
