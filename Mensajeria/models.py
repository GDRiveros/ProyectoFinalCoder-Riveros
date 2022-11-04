from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="remitente")
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinatario")
    mensaje = models.CharField(max_length=100)
    
