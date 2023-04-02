from django.db import models

class Grupo(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=1000)

    def editar(self, variable, nuevo):
        if variable == 'nombre':
            self.nombre = nuevo
        elif variable == 'descripcion':
            self.descripcion = nuevo

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion}"