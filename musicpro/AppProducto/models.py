from django.db import models
from django.db.models.fields import CharField
from django.db.models.deletion import CASCADE

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete = CASCADE)
    codigo = models.CharField(max_length=20, null=False)
    serie_producto = CharField(max_length=20, null=False)
    precio = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre