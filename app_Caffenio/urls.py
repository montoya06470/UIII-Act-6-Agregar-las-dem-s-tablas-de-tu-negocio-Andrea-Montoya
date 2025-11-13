from django.urls import path
from . import views

urlpatterns = [
    # INICIO
    path('', views.inicio, name='inicio'),

    # CATEGORÍAS
    path('categorias/', views.ver_categorias, name='ver_categorias'),
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categoria/actualizar/<int:id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_categoria, name='realizar_actualizacion_categoria'),
    path('categoria/borrar/<int:id>/', views.borrar_categoria, name='borrar_categoria'),

    # PRODUCTOS
    path('productos/', views.ver_productos, name='ver_productos'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),

    # CLIENTES
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # EMPLEADOS
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # PROVEEDORES
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/realizar-actualizacion/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # VENTAS
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),

    # DETALLES DE VENTA
    # ESTA LÍNEA DEBE EXISTIR PARA QUE EL NOMBRE 'ver_detalles_venta' sea válido.
    path('venta/detalles/<int:id>/', views.ver_detalles_venta, name='ver_detalles_venta'), 
    
    path('detalle_venta/agregar/<int:venta_id>/', views.agregar_detalle_venta, name='agregar_detalle_venta'),
    path('detalle_venta/', views.ver_ventas, name='ver_detalle_ventas'),
]