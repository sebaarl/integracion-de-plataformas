from django.shortcuts import render, redirect
from django.db.models.fields import URLField
from tienda.forms import ProductoForm
from AppProducto.models import Producto
from django.contrib.auth.decorators import login_required, permission_required
from django import forms

# Create your views here.
def home(request):
    return render(request, 'tienda/home.html')

def nuevo_producto(request):
    data = {
        'form' :ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        data['forms'] = formulario

    return render(request, 'tienda/nuevo_producto.html', data)