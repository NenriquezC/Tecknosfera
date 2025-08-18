from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
# Clase Categoria
# Si quieres que el campo cliente esté relacionado con un usuario, SIEMPRE usa ForeignKey. Así puedes acceder a todos los datos del usuario y mantener integridad referencial.
User = get_user_model()  # para hacer referencia a un tipo de usuario(cliente o proveedor) que se ha creado en el sistema

#-----------------------------------------------------------------------------------------------------------------------
# Clase Producto
class Compra(models.Model):
    producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE, related_name='compras')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='compras')  # aquí uso el modelo de usuario que se ha creado en el sistema
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(default=timezone.now)

    # Este método __str__ es para que cuando imprimas una instancia de Compra, te muestre el nombre del producto.
    def __str__(self):
        if self.producto: # and  hasattr(self.producto, "nombre"):
            return str(self.producto.nombre)
        else:
            return "Sin producto"

#-----------------------------------------------------------------------------------------------------------------------
# Clase Proveedor
class Compra_Producto(models.Model):
    compra_id = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='compra_productos')
    producto_id = models.ForeignKey('inventario.producto', on_delete=models.CASCADE, related_name='compra_productos')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.compra_id) if self.compra_id is not None else "Sin compra"

#-----------------------------------------------------------------------------------------------------------------------