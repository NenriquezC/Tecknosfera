from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.inicio, name='inicio'),
    path('inventario/', views.inventario, name='inventario'),

    # PRODUCTOS
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),

    # PROVEEDORES
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/eliminar/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedor/eliminar/', views.lista_eliminar_proveedor, name='lista_eliminar_proveedor'), #agregado para eliminar proveedores desde el menu
]