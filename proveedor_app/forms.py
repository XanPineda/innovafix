from django import forms
from .models import Cliente, Usuario, Proveedor, Ingreso, Producto, Venta, Rol, Equipo
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'proveedorNit','telefono','direccion' ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'proveedorNit': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre del Proveedor',
            'proveedorNit': 'NIT del Proveedor',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del proveedor.',
            'proveedorNit': 'Ingrese el NIT del proveedor.',
            'telefono': 'Ingrese el número de teléfono del proveedor.',
            'direccion': 'Ingrese la dirección del proveedor.',
        }


class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        # Campos en el orden deseado
        fields = ['usuCedula', 'proveedorNit', 'ingresoValor', 'ingresoCantidad']
        # Labels más amigables
        labels = {
            'usuCedula': 'Nombre Usuario',
            'proveedorNit': 'Proveedor',
            'ingresoValor': 'Valor',
            'ingresoCantidad': 'Cantidad',
        }
        widgets = {
            'usuCedula': forms.Select(attrs={'class': 'form-control'}),
            'proveedorNit': forms.Select(attrs={'class': 'form-control'}),
            'ingresoValor': forms.NumberInput(attrs={'class': 'form-control'}),
            'ingresoCantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['clienteCedula', 'clienteNombre', 'clienteApellido', 'clienteUsuario',
        'clienteContrasena', 'clienteFoto', 'clienteCorreo', 'clienteTelefono',
        'clienteDireccion']
        widgets = {
            'clienteCedula': forms.TextInput(attrs={'class': 'form-control'}),
            'clienteNombre': forms.TextInput(attrs={'class': 'form-control'}),
            'clienteApellido': forms.TextInput(attrs={'class': 'form-control'}),
            'clienteUsuario': forms.TextInput(attrs={'class': 'form-control'}),
            'clienteContrasena': forms.PasswordInput(attrs={'class': 'form-control'}),
            'clienteFoto': forms.FileInput(attrs={'class': 'form-control'}),
            'clienteCorreo': forms.EmailInput(attrs={'class': 'form-control'}),
            'clienteTelefono': forms.TextInput(attrs={'class': 'form-control'}),
            'clienteDireccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'clienteCedula': 'Cedula',
            'clienteNombre': 'Nombre',
            'clienteApellido': 'Apellido',
            'clienteUsuario': 'Usuario',
            'clienteContrasena': 'Contraseña',
            'clienteFoto': 'Foto de perfil',
            'clienteCorreo': 'Correo electrónico',
            'clienteTelefono': 'Número de teléfono',
            'clienteDireccion': 'Dirección',
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'usuCedula', 'usuUsuario', 'usuNombre', 'usuApellido',
            'usuContrasena', 'usuCorreo', 'usuTelefono',
            'usuDireccion', 'usuFoto'
        ]
        widgets = {
            'usuCedula': forms.TextInput(attrs={'class': 'form-control'}),
            'usuUsuario': forms.TextInput(attrs={'class': 'form-control'}),
            'usuNombre': forms.TextInput(attrs={'class': 'form-control'}),
            'usuApellido': forms.TextInput(attrs={'class': 'form-control'}),
            'usuContrasena': forms.PasswordInput(attrs={'class': 'form-control'}),
            'usuCorreo': forms.EmailInput(attrs={'class': 'form-control'}),
            'usuTelefono': forms.TextInput(attrs={'class': 'form-control'}),
            'usuDireccion': forms.TextInput(attrs={'class': 'form-control'}),
            'usuFoto': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'usuCedula': 'Cédula',
            'usuUsuario': 'Nombre de Usuario',
            'usuNombre': 'Nombre',
            'usuApellido': 'Apellido',
            'usuContrasena': 'Contraseña',
            'usuCorreo': 'Correo Electrónico',
            'usuTelefono': 'Teléfono',
            'usuDireccion': 'Dirección',
            'usuFoto': 'Foto de Perfil (URL o archivo)',
        }

class RolForm (forms.ModelForm):
    class Meta:
        model = Rol
        fields = [ 
            'rolNombre', 'rolDescripcion',
        ]
        widgets = {
            'rolNombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rolDescripcion': forms.Textarea(attrs={'class': 'form-control'})
            }
        labels = {
            'rolNombre': 'Nombre del Rol',
            'rolDescripcion': 'Descripción del Rol',
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['productoId']  # ✅ Se asigna automáticamente en la vista

        labels = {
            'productoNombre': 'Nombre del Producto',
            'productoPrecioUnidad': 'Precio Unitario',
            'productoCantidad': 'Cantidad',
            'productoDescripcion': 'Descripción',
            'ingreso': 'Ingreso Asociado',
        }

        widgets = {
            'productoNombre': forms.TextInput(attrs={'class': 'form-control'}),
            'productoPrecioUnidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'productoCantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'productoDescripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'ingreso': forms.Select(attrs={'class': 'form-control'}),  # ✅ Campo obligatorio
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingreso'].required = True
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        exclude = ['ventaId', 'usuCedula']  

        widgets = {
            'ventaCantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'ventaTipoProducto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Opcional'
            }),
            'ventaMetodoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'ventaPrecio': forms.NumberInput(attrs={'class': 'form-control'}),
            'productoId': forms.Select(attrs={'class': 'form-control'}),
            'clienteCedula': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'ventaCantidad': 'Cantidad Vendida',
            'ventaTipoProducto': 'Tipo de Producto (opcional)',
            'ventaMetodoPago': 'Método de Pago',
            'ventaPrecio': 'Precio Total',
            'productoId': 'Producto',
            'clienteCedula': 'Cliente',
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['equipoRef', 'equipoNovedad', 'clienteNombre', 'usuNombre', 'equipoEstado']
        labels = {
            'equipoRef': 'Referencia del Equipo',
            'equipoNovedad': 'Novedad del Equipo',
            'clienteNombre': 'Cliente',
            'usuNombre': 'Usuario',
            'equipoEstado': 'Estado',
        }
        widgets = {
            'equipoRef': forms.TextInput(attrs={'class': 'form-control'}),
            'equipoNovedad': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'clienteNombre': forms.Select(attrs={'class': 'form-control'}),
            'usuNombre': forms.Select(attrs={'class': 'form-control'}),
            'equipoEstado': forms.Select(attrs={'class': 'form-control'}),
        }

# Formset para Productos asociados al Ingreso
ProductoFormSet = inlineformset_factory(
    Ingreso,
    Producto,
    form=ProductoForm,
    extra=0,         
    can_delete=True  
)