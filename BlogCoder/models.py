from django.db import models

# Create your models here.

class Blog(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=100)
    fecha = models.DateField(null=True)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} de {self.autor}"

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
