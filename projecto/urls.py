"""projecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion.views import *
from grupo.views import *
from publicacion.views import *

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', mostrarUsuarios, name="usuarios-list"),
    path('usuarios/agregar', agregarUsuario, name="usuario-create"),
    path('usuario/borrar/<id>', borrarUsuario, name="usuario-delete"),
    path('usuarioBuscar', buscarUsuario, name="usuario-search"),
    path('usuarioEditar/<id>', editarUsuario, name='usuario-edit'),
    path('grupo/', mostrarGrupos, name="grupos-list"),
    path('grupo/agregar', agregarGrupo, name="grupo-create"),
    path('grupo/borrar/<id>', borrarGrupo, name="grupo-delete"),
    path('grupoBuscar', buscarGrupo, name="grupo-search"),
    path('grupoEditar/<id>', editarGrupo, name='grupo-edit'), 
    path('publicacion/', mostrarPublicaciones, name="publicaion-list"),
    path('publicacion/agregar', agregarPublicacion, name="publicacion-create"),
    path('publicacion/borrar/<id>', borrarPublicacion, name="publicacion-delete"),
    path('publicacionBuscar', buscarPublicacion, name="publicacion-search"),
    path('publicacionEditar/<id>', editarPublicacion, name='publicacion-edit'), 
]