from django.db import models

# Create your models here.

class Usuario(models.Model):
    user = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()