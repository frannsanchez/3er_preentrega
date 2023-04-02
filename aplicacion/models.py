from django.db import models

class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    usuario = models.TextField(max_length=100)
    contrasena = models.TextField(max_length=100)
    grupo = models.TextField(max_length=100)

    def editar(self, variable, nuevo):
        if variable == 'nombre':
            self.nombre = nuevo
        elif variable == 'usuario':
            self.usuario = nuevo
        elif variable == 'contrasena':
            self.contrasena = nuevo
        elif variable == 'grupo':
            self.grupo = nuevo
        

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.grupo}"




