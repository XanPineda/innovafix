from django.db import models
from django.contrib.auth.models import User

class VistaIngresoInfo(models.Model):
    ingresoId = models.IntegerField(primary_key=True)
    ingresoValor = models.IntegerField()
    ingresoCantidad = models.IntegerField()
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    usuNombre = models.CharField(max_length=25)
    usuApellido = models.CharField(max_length=25)
    usuCorreo = models.EmailField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ingresoinfo'


class VistaCompraVenta(models.Model):
    clienteNombre = models.CharField(max_length=25)
    ventaId = models.CharField(max_length=20, primary_key=True)
    ventaCantidad = models.IntegerField()
    productoNombre = models.CharField(max_length=25)
    productoPrecioUnidad = models.IntegerField()
    class Meta:

        managed = False
        db_table = 'compraventa'

class VistaProcesoIngreso(models.Model):
    usuNombre = models.CharField(max_length=25)
    ingresoId = models.IntegerField(primary_key=True)
    ingresoValor = models.IntegerField()
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'procesoingreso'

class Rol (models.Model):
    rolId = models.AutoField(primary_key=True)
    rolNombre = models.CharField(max_length=20)
    rolDescripcion = models.CharField(max_length=150)

    class Meta:
        db_table = 'Rol'

    def __str__(self):
        return self.rolNombre

class Cliente(models.Model):
    clienteCedula = models.CharField(max_length=10, primary_key=True)
    clienteNombre = models.CharField(max_length=25)
    clienteApellido = models.CharField(max_length=25)
    clienteUsuario = models.CharField(max_length=10)
    clienteContrasena = models.CharField(max_length=10)
    clienteFoto = models.ImageField(upload_to='fotos_usuarios/', blank=True, null=True)
    clienteCorreo = models.EmailField(max_length=50)
    clienteTelefono = models.CharField(max_length=10)
    clienteDireccion = models.CharField(max_length=40)

    class Meta:
        db_table = 'Cliente'

    def __str__(self):
        return f"{self.clienteNombre} {self.clienteApellido}"



class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    proveedorNit = models.CharField(max_length=10, primary_key=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre


class Ingreso(models.Model):
    ingresoId = models.AutoField(primary_key=True)
    ingresoValor = models.IntegerField()
    ingresoCantidad = models.IntegerField()
    proveedorNit = models.ForeignKey('Proveedor', to_field='proveedorNit', on_delete=models.CASCADE, db_column='proveedorNit')
    usuCedula = models.ForeignKey('Usuario', to_field='usuCedula', on_delete=models.CASCADE, db_column='usuCedula')

    class Meta:
        db_table = 'ingreso'

    def __str__(self):
        return f"{self.ingresoId} - {self.proveedorNit.proveedorNit} - {self.ingresoValor}"


class Usuario(models.Model):
    usuCedula = models.CharField(max_length=10, primary_key=True)
    usuUsuario = models.CharField(max_length=10)
    usuNombre = models.CharField(max_length=25)
    usuApellido = models.CharField(max_length=25)
    usuContrasena = models.CharField(max_length=10)
    usuCorreo = models.EmailField(max_length=35)
    usuTelefono = models.CharField(max_length=10)
    usuDireccion = models.CharField(max_length=30)
    usuFoto = models.ImageField(upload_to='fotos_usuarios/', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.usuNombre} {self.usuApellido}"


class Producto(models.Model):
    productoId = models.CharField(max_length=10, primary_key=True)
    productoNombre = models.CharField(max_length=25)
    productoPrecioUnidad = models.IntegerField()
    productoCantidad = models.IntegerField()
    productoDescripcion = models.CharField(max_length=225)
    ingreso = models.ForeignKey('Ingreso', on_delete=models.CASCADE, db_column='ingresoId')

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.productoNombre

class Venta(models.Model):
    ventaId = models.CharField(max_length=20, primary_key=True)
    ventaCantidad = models.IntegerField()
    ventaTipoProducto = models.CharField(max_length=20, blank=True, null=True)  # Campo opcional
    ventaMetodoPago = models.CharField(max_length=20)
    ventaPrecio = models.IntegerField()
    productoId = models.ForeignKey('Producto', to_field='productoId', on_delete=models.CASCADE, db_column='productoId')
    clienteCedula = models.ForeignKey('Cliente', to_field='clienteCedula', on_delete=models.CASCADE, db_column='clienteCedula')
    usuCedula = models.ForeignKey('Usuario', to_field='usuCedula', on_delete=models.CASCADE, db_column='usuCedula')

    class Meta:
        db_table = 'venta'

    def __str__(self):
        return f"Venta {self.ventaId} - Cliente {self.clienteCedula}"
    