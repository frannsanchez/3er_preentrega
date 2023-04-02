from django.db import models

class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    usuario = models.TextField(max_length=100)
    contrasena = models.TextField(max_length=100)
    grupo = models.TextField(max_length=100)

    def editar(self):
        self.variable = nuevo
        

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.grupo}"

    

class Publicacion(models.Model):
    usuario = models.TextField(max_length=100)
    titulo = models.TextField(max_length=200)
    cuerpo = models.TextField(max_length=1000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.titulo} - {self.cuerpo} - {self.usuario} - {self.fecha_publicacion}"
    


class Grupo(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion}"
