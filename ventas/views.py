from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from inventario.models import Producto #marca en rojo es unf also positivo
from .forms import VentaForm
from django.contrib import messages

# Create your views here.
#-----------------------------------------------------------------------------------------------------------------------
def agregar_venta(request):
    """
    :param request:
    :return:
    """
    if request.method == 'POST': # Verifica si el método de la solicitud es POST
        # Si el método es POST, significa que se está enviando el formulario
        # Aquí se procesa el formulario de venta
        form = VentaForm(request.POST) # Crea una instancia del formulario con los datos enviados
        if form.is_valid(): # Verifica si el formulario es válido
            venta = form.save(commit=False) # No guarda aún en la base de datos
            producto = venta.producto # Obtiene el producto de la venta
            producto.stock -= venta.cantidad  # Disminuye el stock del producto
            if producto.stock < 0: # Verifica si el stock es negativo
                messages.error(request, 'No hay suficiente stock para realizar la venta.') # Muestra un mensaje de error
                return redirect('ventas:agregar_venta') # Redirige para evitar el doble submit
            producto.save()  # Guarda el producto con el nuevo stock
            form.save() # Guarda la venta en la base de datos
            messages.success(request, '¡Venta registrada exitosamente!') # Muestra un mensaje de éxito
            return redirect('/ventas/agregar/?exito=1') # Redirige y pasa un parámetro GET para mostrar el modal
    else:
        form = VentaForm() # Si el método no es POST, crea un formulario vacío
    productos = Producto.objects.all() # Obtiene todos los productos disponibles
    return render(request, 'agregar_venta.html', {'form': form, 'productos': productos})
    # Renderiza la plantilla con el formulario y los productos disponibles

#-----------------------------------------------------------------------------------------------------------------------
def ver_ventas(request):
    """
    :param request:
    :return: render con las ventas ordenadas por fecha
    """
    ventas = Venta.objects.select_related('producto', 'cliente').order_by('-fecha')
    return render(request, 'ver_ventas.html', {'ventas': ventas})
#-----------------------------------------------------------------------------------------------------------------------
def editar_venta(request, venta_id):
    """
    :param request:
    :param venta_id: ID de la venta a editar
    :return: render con el formulario para editar la venta
    """
    venta = get_object_or_404(Venta, id=venta_id) # Obtiene la venta a editar o muestra un error 404 si no existe
    if request.method == 'POST': # Si el método es POST, significa que se está enviando el formulario
        form = VentaForm(request.POST, instance=venta) # Crea una instancia del formulario con los datos enviados y la venta existente
        if form.is_valid(): # Verifica si el formulario es válido
            form.save() # Guarda la venta actualizada en la base de datos
            messages.success(request, '¡Venta actualizada exitosamente!') # Muestra un mensaje de éxito
            return redirect('ventas:ver_ventas') # Redirige a la vista de ventas después de actualizar
    else:
        form = VentaForm(instance=venta) # Si el método no es POST, crea un formulario con los datos de la venta existente
    return render(request, 'editar_venta.html', {'form': form, 'venta': venta})
    # Renderiza la plantilla con el formulario y la venta a editar
#-----------------------------------------------------------------------------------------------------------------------
def eliminar_venta(request, venta_id):
    """
    :param request:
    :param venta_id: ID de la venta a eliminar
    :return: redirige a la vista de ventas después de eliminar
    """
    venta = get_object_or_404(Venta, id=venta_id) # Obtiene la venta a eliminar o muestra un error 404 si no existe
    venta.delete() # Elimina la venta de la base de datos
    messages.success(request, '¡Venta eliminada exitosamente!') # Muestra un mensaje de éxito
    return redirect('ventas:ver_ventas') # Redirige a la vista de ventas después de eliminar
#-----------------------------------------------------------------------------------------------------------------------
def seleccionar_editar_venta(request):
    """
    :param request:
    :return: render con el formulario para seleccionar una venta a editar
    """
    ventas = Venta.objects.all()  # Obtiene todas las compras
    buscar = request.GET.get("buscar")  # Obtiene el parámetro de búsqueda de la URL
    if buscar:  # Si hay un término de búsqueda
        compras = ventas.filter(  # Filtra las compras por el nombre del producto, nombre del cliente o ID
            producto__nombre__icontains=buscar
        ) | ventas.filter(
            cliente__nombre__icontains=buscar
        ) | ventas.filter(
            id__icontains=buscar
        )
    return render(request, 'seleccionar_editar_venta.html', {'ventas': ventas})
    # Renderiza la plantilla con las ventas disponibles para seleccionar
#-----------------------------------------------------------------------------------------------------------------------
def seleccionar_eliminar_venta(request):
    """
    :param request:
    :return: render con el formulario para seleccionar una venta a eliminar
    """
    ventas = Venta.objects.all()  # Obtiene todas las compras
    buscar = request.GET.get("buscar")  # Obtiene el parámetro de búsqueda de la URL
    if buscar:  # Si hay un término de búsqueda
        ventas = ventas.filter(  # Filtra las compras por el nombre del producto, nombre del cliente o ID
            producto__nombre__icontains=buscar
        ) | ventas.filter(
            cliente__nombre__icontains=buscar
        ) | ventas.filter(
            id__icontains=buscar
        )
    return render(request, 'seleccionar_eliminar_venta.html', {'ventas': ventas})
    # Renderiza la plantilla con las ventas disponibles para seleccionar
#-----------------------------------------------------------------------------------------------------------------------