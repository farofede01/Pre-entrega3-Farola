from django.db import models

# Create your models here.

class Medicos (models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre}-{self.dni}-{self.email}"

class Hospitales (models.Model):
    nombre = models.CharField(max_length=50)
    num_telefono = models.CharField(max_length=50)
    direccion = models.CharField (max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre}-{self.num_telefono}-{self.direccion}-{self.email}"

class Obrasocial (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre}-{self.costo}-{self.email}"
     
    
    