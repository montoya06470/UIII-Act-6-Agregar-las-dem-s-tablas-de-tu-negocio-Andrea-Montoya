from django.db import models

# ==========================================
# CATEGORÍA (7 campos)
# ==========================================
class Categoria(models.Model):
    nombre_categoria = models.CharField(
        max_length=30,
        choices=[
            ('cafe_caliente', 'Café Caliente'),
            ('cafe_frio', 'Café Frío'),
            ('sin_cafe', 'Bebidas Sin Café'),
            ('alimentos', 'Alimentos'),
            ('panaderia', 'Panadería'),
            ('mercancia', 'Mercancía')
        ]
    )
    descripcion = models.TextField()                    # 1
    icono = models.CharField(max_length=50, blank=True) # 2
    orden = models.IntegerField(default=0)              # 3
    color = models.CharField(max_length=7, default='#6c757d')  # 4
    activa = models.BooleanField(default=True)          # 5
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # 6
    # 7º CAMPO: **NOMBRE MOSTRADO EN SELECTS**
    # → Ya está con `get_nombre_categoria_display`

    def __str__(self):
        return self.get_nombre_categoria_display()

# ==========================================
# CLIENTE (7 campos)
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)
    tipo_cliente = models.CharField(max_length=20, choices=[('regular', 'Regular'), ('frecuente', 'Frecuente'), ('nuevo', 'Nuevo')], default='nuevo')
    notas = models.TextField(blank=True)

    def __str__(self): return self.nombre

# ==========================================
# EMPLEADO (7 campos)
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=20, choices=[('cajero', 'Cajero'), ('barista', 'Barista'), ('gerente', 'Gerente'), ('supervisor', 'Supervisor'), ('limpieza', 'Limpieza'), ('seguridad', 'Seguridad')])
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self): return f"{self.nombre} - {self.get_puesto_display()}"

# ==========================================
# PROVEEDOR (7 campos)
# ==========================================
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50, choices=[('bebidas', 'Bebidas'), ('alimentos', 'Alimentos'), ('complementos', 'Complementos')])

    def __str__(self): return f"{self.nombre} - {self.empresa}"

# ==========================================
# PRODUCTO (7 campos)
# ==========================================
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    sucursal = models.CharField(max_length=50, choices=[('Sucursal 1', 'Sucursal 1'), ('Sucursal 2', 'Sucursal 2')])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self): return self.nombre

# ==========================================
# VENTA (7 campos)
# ==========================================
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='ventas')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')])
    sucursal = models.CharField(max_length=50, choices=[('Sucursal 1', 'Sucursal 1'), ('Sucursal 2', 'Sucursal 2')])
    estado = models.CharField(max_length=20, choices=[('completada', 'Completada'), ('pendiente', 'Pendiente'), ('cancelada', 'Cancelada')], default='completada')

    def __str__(self): return f"Venta #{self.id}"

# ==========================================
# DETALLE VENTA (7 campos)
# ==========================================
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalleventa_set')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    nota = models.TextField(blank=True)

    def subtotal(self):
        return self.cantidad * self.precio_unitario * (1 - self.descuento / 100)

    def save(self, *args, **kwargs):
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        self.subtotal = self.cantidad * self.precio_unitario * (1 - self.descuento / 100)
        super().save(*args, **kwargs)

    def __str__(self): return f"{self.cantidad}x {self.producto.nombre}"