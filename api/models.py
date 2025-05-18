from django.db import models

# Create your models here.
class Mascotas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='mascotas/')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.especie} - {self.raza}"
