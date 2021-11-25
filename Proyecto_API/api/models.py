from django.db import models

# Create your models here.

class Usuario(models.Model):
    correo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)