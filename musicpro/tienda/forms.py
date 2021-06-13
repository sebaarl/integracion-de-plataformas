from django import forms
from django.forms import ModelForm, fields, models
from AppProducto.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'codigo', 'serie_producto', 'precio', 'descripcion']