from django.urls import path
from . import views


app_name = 'ventas'

urlpatterns = [
    path('agregar/', views.agregar_venta, name='agregar_venta'),
    path('ver/', views.ver_ventas, name='ver_ventas'),
    path('editar/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    path('seleccionar_editar/', views.seleccionar_editar_venta, name='seleccionar_editar_venta'),
    path('seleccionar_eliminar/', views.seleccionar_eliminar_venta, name='seleccionar_eliminar_venta'),
]
