from django.shortcuts import render
from django.http import HttpResponse
from grupo.models import Grupo

def mostrarGrupos(request):
    grupos = Grupo.objects.all()
    return render(request, "grupo/grupo.html", {"grupos": grupos})

def agregarGrupo(request):
    nombreU = request.GET.get("nombre")
    descripcionU = request.GET.get("descripcion")
    nuevoGrupo = Grupo(nombre=nombreU, descripcion = descripcionU)
    nuevoGrupo.save()
    return mostrarGrupos(request)

def borrarGrupo(request, id):
    grupo = Grupo.objects.filter(id=id).first()
    grupo.delete()
    return mostrarGrupos(request)

def buscarGrupo(request):
    criterio = request.GET.get("buscar")
    if criterio:
        grupos = Grupo.objects.filter(nombre__icontains = criterio).all()
        return render(request, "grupo/grupoBuscar.html", {"grupos":grupos})
    return render(request, "grupo/grupoBuscar.html")

def editarGrupo(request, id): 
    grupo = Grupo.objects.filter(id=id).first()
    if request.method == 'POST':
        variable = request.POST.get('variable')
        nuevo = request.POST.get('nuevo')
        grupo.editar(variable, nuevo)
        grupo.save()
        return mostrarGrupos(request)
    return render(request, 'grupo/grupoEditar.html', {'grupo': grupo})