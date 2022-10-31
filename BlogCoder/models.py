from django.db import models
from django.contrib.auth.models import User



class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Blog(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=100)
    fecha = models.DateField(null=True)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} de {self.autor}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)






