from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Categoria, Producto, Proveedor, Cliente, Empleado,
    Venta, DetalleVenta
)
from decimal import Decimal # 👈 ¡Importación necesaria para manejo seguro de dinero!

# ==================== INICIO ====================
def inicio(request):
    return render(request, 'inicio.html')

# ==================== CATEGORÍAS ====================
def ver_categorias(request):
    categorias = Categoria.objects.all().order_by('orden')
    return render(request, 'categoria/ver_categorias.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        Categoria.objects.create(
            nombre_categoria=request.POST['nombre_categoria'],
            descripcion=request.POST['descripcion'],
            icono=request.POST.get('icono', ''),
            orden=request.POST.get('orden', 0),
            color=request.POST.get('color', '#6c757d'),
            activa='activa' in request.POST
        )
        return redirect('ver_categorias')
    return render(request, 'categoria/agregar_categoria.html')

def actualizar_categoria(request, id):
    cat = get_object_or_404(Categoria, id=id)
    return render(request, 'categoria/actualizar_categoria.html', {'categoria': cat})

def realizar_actualizacion_categoria(request, id):
    cat = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        cat.nombre_categoria = request.POST['nombre_categoria']
        cat.descripcion = request.POST['descripcion']
        cat.icono = request.POST.get('icono', '')
        cat.orden = request.POST.get('orden', 0)
        cat.color = request.POST.get('color', '#6c757d')
        cat.activa = 'activa' in request.POST
        cat.save()
        return redirect('ver_categorias')
    return redirect('actualizar_categoria', id=id)

def borrar_categoria(request, id):
    cat = get_object_or_404(Categoria, id=id)
    cat.delete()
    return redirect('ver_categorias')

# ==================== PRODUCTOS ====================
def ver_productos(request):
    productos = Producto.objects.select_related('categoria', 'proveedor').all()
    # ⚠️ Asegúrate de que 'producto/ver_productos.html' exista en la carpeta templates
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            categoria_id=request.POST['categoria'],
            proveedor_id=request.POST['proveedor'],
            sucursal=request.POST['sucursal']
        )
        return redirect('ver_productos')
    return render(request, 'producto/agregar_producto.html', {
        'categorias': Categoria.objects.all(),
        'proveedores': Proveedor.objects.all()
    })

def actualizar_producto(request, id):
    prod = get_object_or_404(Producto, id=id)
    return render(request, 'producto/actualizar_producto.html', {
        'producto': prod,
        'categorias': Categoria.objects.all(),
        'proveedores': Proveedor.objects.all()
    })

def realizar_actualizacion_producto(request, id):
    p = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        p.nombre = request.POST['nombre']
        p.descripcion = request.POST['descripcion']
        p.precio = request.POST['precio']
        p.stock = request.POST['stock']
        p.categoria_id = request.POST['categoria']
        p.proveedor_id = request.POST['proveedor']
        p.sucursal = request.POST['sucursal']
        p.save()
        return redirect('ver_productos')
    return redirect('actualizar_producto', id=id)

def borrar_producto(request, id):
    prod = get_object_or_404(Producto, id=id)
    prod.delete()
    return redirect('ver_productos')

# ==================== CLIENTES ====================
def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            direccion=request.POST['direccion']
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, id):
    cli = get_object_or_404(Cliente, id=id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cli})

def realizar_actualizacion_cliente(request, id):
    cli = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cli.nombre = request.POST['nombre']
        cli.apellido = request.POST['apellido']
        cli.telefono = request.POST['telefono']
        cli.email = request.POST['email']
        cli.direccion = request.POST['direccion']
        cli.save()
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', id=id)

def borrar_cliente(request, id):
    cli = get_object_or_404(Cliente, id=id)
    cli.delete()
    return redirect('ver_clientes')

# ==================== EMPLEADOS ====================
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            puesto=request.POST['puesto'],
            sucursal=request.POST['sucursal'],
            fecha_contratacion=request.POST['fecha_contratacion'],
            salario=request.POST['salario'],
            activo='activo' in request.POST
        )
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleado(request, id):
    emp = get_object_or_404(Empleado, id=id)
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': emp})

def realizar_actualizacion_empleado(request, id):
    emp = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        emp.nombre = request.POST['nombre']
        emp.apellido = request.POST['apellido']
        emp.telefono = request.POST['telefono']
        emp.email = request.POST['email']
        emp.puesto = request.POST['puesto']
        emp.sucursal = request.POST['sucursal']
        emp.fecha_contratacion = request.POST['fecha_contratacion']
        emp.salario = request.POST['salario']
        emp.activo = 'activo' in request.POST
        emp.save()
        return redirect('ver_empleados')
    return redirect('actualizar_empleado', id=id)

def borrar_empleado(request, id):
    emp = get_object_or_404(Empleado, id=id)
    emp.delete()
    return redirect('ver_empleados')

# ==================== PROVEEDORES ====================
def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        Proveedor.objects.create(
            nombre=request.POST['nombre'],
            empresa=request.POST['empresa'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            direccion=request.POST['direccion'],
            activo='activo' in request.POST
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def actualizar_proveedor(request, id):
    prov = get_object_or_404(Proveedor, id=id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': prov})

def realizar_actualizacion_proveedor(request, id):
    prov = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        prov.nombre = request.POST['nombre']
        prov.empresa = request.POST['empresa']
        prov.telefono = request.POST['telefono']
        prov.email = request.POST['email']
        prov.direccion = request.POST['direccion']
        prov.activo = 'activo' in request.POST
        prov.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', id=id)

def borrar_proveedor(request, id):
    prov = get_object_or_404(Proveedor, id=id)
    prov.delete()
    return redirect('ver_proveedores')

# ==================== VENTAS ====================
def ver_ventas(request):
    ventas = Venta.objects.select_related('cliente', 'empleado') \
                           .prefetch_related('detalleventa_set__producto') \
                           .all().order_by('-fecha')
    return render(request, 'venta/ver_venta.html', {'ventas': ventas})

def agregar_venta(request):
    if request.method == 'POST':
        venta = Venta.objects.create(
            cliente_id=request.POST['cliente'],
            empleado_id=request.POST['empleado'],
            total=request.POST['total'],
            metodo_pago=request.POST['metodo_pago'],
            sucursal=request.POST['sucursal'],
            estado=request.POST['estado']
        )
        productos = request.POST.getlist('producto_id')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')

        max_len = min(len(productos), len(cantidades), len(precios))
        for i in range(max_len):
            if productos[i] and cantidades[i] and precios[i]:
                
                # 🟢 CORRECCIÓN: Conversión a int y Decimal para evitar TypeError
                try:
                    cantidad_int = int(cantidades[i])
                    precio_dec = Decimal(precios[i].replace('$', ''))
                except ValueError:
                    # Ignora la fila si los datos no son válidos
                    continue

                DetalleVenta.objects.create(
                    venta=venta,
                    producto_id=productos[i],
                    cantidad=cantidad_int,
                    precio_unitario=precio_dec
                )
        return redirect('ver_ventas')

    return render(request, 'venta/agregar_venta.html', {
        'clientes': Cliente.objects.all(),
        'empleados': Empleado.objects.all(),
        'productos': Producto.objects.all()
    })

def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    detalles = venta.detalleventa_set.select_related('producto').all()

    if request.method == 'POST':
        venta.cliente_id = request.POST['cliente']
        venta.empleado_id = request.POST['empleado']
        venta.total = request.POST['total']
        venta.metodo_pago = request.POST['metodo_pago']
        venta.sucursal = request.POST['sucursal']
        venta.estado = request.POST['estado']
        venta.save()

        # Borrar detalles antiguos antes de crear los nuevos
        venta.detalleventa_set.all().delete()

        productos = request.POST.getlist('producto_id')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')

        max_len = min(len(productos), len(cantidades), len(precios))
        for i in range(max_len):
            if productos[i] and cantidades[i] and precios[i]:
                
                # 🟢 CORRECCIÓN: Conversión a int y Decimal para evitar TypeError
                try:
                    cantidad_int = int(cantidades[i])
                    precio_dec = Decimal(precios[i].replace('$', ''))
                except ValueError:
                    # Ignora la fila si los datos no son válidos
                    continue

                DetalleVenta.objects.create(
                    venta=venta,
                    producto_id=productos[i],
                    cantidad=cantidad_int,
                    precio_unitario=precio_dec
                )
        return redirect('ver_ventas')

    return render(request, 'venta/actualizar_venta.html', {
        'venta': venta,
        'detalles': detalles,
        'clientes': Cliente.objects.all(),
        'empleados': Empleado.objects.all(),
        'productos': Producto.objects.all()
    })

def borrar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    venta.delete()
    return redirect('ver_ventas')

# ==================== DETALLES DE VENTA ====================
def ver_detalles_venta(request, id):
    venta = get_object_or_404(Venta.objects.select_related('cliente', 'empleado'), id=id)
    detalles = venta.detalleventa_set.select_related('producto').all()
    context = {
        'venta': venta,
        'detalles': detalles
    }
    return render(request, 'detalle_venta/ver_detalles_venta.html', context)


def agregar_detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        # Aseguramos la conversión aquí también si este formulario se usa
        try:
            precio_dec = Decimal(request.POST['precio_unitario'])
            cantidad_int = int(request.POST['cantidad'])
        except ValueError:
            return redirect('ver_detalles_venta', id=venta_id) # O manejar el error
            
        DetalleVenta.objects.create(
            venta=venta,
            producto_id=request.POST['producto'],
            cantidad=cantidad_int,
            precio_unitario=precio_dec,
            descuento=request.POST.get('descuento', 0),
            nota=request.POST.get('nota', '')
        )
        return redirect('ver_ventas')
    return render(request, 'detalle_venta/agregar_detalle.html', {
        'venta': venta,
        'productos': Producto.objects.all()
    })