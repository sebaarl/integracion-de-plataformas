from django.urls import path
from tienda.views import nuevo_producto, home

urlpatterns = [
    path('', home, name="home"),
    path('nuevo-producto/', nuevo_producto, name='nuevo_producto'),
]