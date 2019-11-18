from django.db import models
#from django.contrib.auth.models import User

class Alumno(models.Model):
#    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=60)
    imagen = models.ImageField(null=True, upload_to="fotos/")
    curso = models.ManyToManyField('Curso', null=True)
    

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"
    def get_dni(self):
        return self.dni

class Curso(models.Model):
    abrev = models.CharField(max_length=10, primary_key=True)
    denom = models.CharField(max_length=40)
    imagen = models.ImageField(null=True, upload_to="fotos/")

    def __str__(self):
        return self.denom
