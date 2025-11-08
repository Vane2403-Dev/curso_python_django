from django.db import models

# Create your models here.
from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Lista(models.Model):
    nombre = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="listas")

    def __str__(self):
        return f"{self.nombre} ({self.proyecto.nombre})"


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name="tareas")
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo