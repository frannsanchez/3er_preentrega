from django.db import models

class Publicacion(models.Model):
    usuario = models.TextField(max_length=100)
    titulo = models.TextField(max_length=200)
    cuerpo = models.TextField(max_length=1000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def editar(self, variable, nuevo):
        if variable == 'usuario':
            self.nombre = nuevo
        elif variable == 'titulo':
            self.usuario = nuevo
        elif variable == 'cuerpo':
            self.contrasena = nuevo
    
    def __str__(self):
        return f"{self.id} - {self.titulo} - {self.cuerpo} - {self.usuario} - {self.fecha_publicacion}"
    