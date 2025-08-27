from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Rol, Proveedor, Cliente, Usuario, Ingreso, Producto, Venta, VistaIngresoInfo, VistaCompraVenta, VistaProcesoIngreso
from .forms import RolForm, ProveedorForm, ClienteForm, UsuarioForm, IngresoForm, ProductoForm, VentaForm
from django.contrib import messages

# RENDERIZADO DE HOME PAGE
def homepage(request):
    return render(request, 'homepage.html')


# RENDERIZADO DE INICIO
@login_required
def inicio(request):
    return render(request, 'inicio.html')  

#----------------------------
#VISTA 
#----------------------------

@login_required
def vista_ingreso_info_listar(request):
    datos = VistaIngresoInfo.objects.all()
    return render(request, 'proveedor/reportes/vista_ingreso_info.html', {'datos': datos})

#Exportar a Excel
def exportar_ingreso_info_excel(request):
    from django.http import HttpResponse
    import pandas as pd

    # Obtener los datos de la vista
    datos = VistaIngresoInfo.objects.all()

    # Crear un DataFrame de pandas
    data = {
        'ID': [dato.ingresoId for dato in datos],
        'Valor': [dato.ingresoValor for dato in datos],
        'Cantidad': [dato.ingresoCantidad for dato in datos],
        'Nombre': [dato.nombre for dato in datos],
        'Dirección': [dato.direccion for dato in datos],
        'Usuario Nombre': [dato.usuNombre for dato in datos],
        'Usuario Apellido': [dato.usuApellido for dato in datos],
        'Usuario Correo': [dato.usuCorreo for dato in datos],
    }
    df = pd.DataFrame(data)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ingreso_info.xlsx"'

    # Exportar a Excel
    df.to_excel(response, index=False)

    return response

# Exportar a PDF
def exportar_ingreso_info_pdf(request):
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa

    # Obtener los datos de la vista
    datos = VistaIngresoInfo.objects.all()

    # Cargar la plantilla HTML
    template = get_template('proveedor/reportes/reporte_ingresoInfo_pdf.html')
    context = {
        'datos': datos,
    }
    html = template.render(context)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ingreso_info.pdf"'

    # Convertir HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    
    return response

@login_required
def vista_compra_venta_listar(request):
    datos = VistaCompraVenta.objects.all()
    return render(request, 'proveedor/reportes/vista_compra_venta.html', {'datos': datos})

# Exportar a Excel
def exportar_compra_venta_excel(request):
    from django.http import HttpResponse
    import pandas as pd

    # Obtener los datos de la vista
    datos = VistaCompraVenta.objects.all()

    # Crear un DataFrame de pandas
    data = {
        'Cliente Nombre': [dato.clienteNombre for dato in datos],
        'ID Venta': [dato.ventaId for dato in datos],
        'Cantidad': [dato.ventaCantidad for dato in datos],
        'Producto Nombre': [dato.productoNombre for dato in datos],
        'Producto Precio Unidad': [dato.productoPrecioUnidad for dato in datos],
    }
    df = pd.DataFrame(data)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="compra_venta.xlsx"'

    # Exportar a Excel
    df.to_excel(response, index=False)

    return response

# Exportar a PDF
def exportar_compra_venta_pdf(request):
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa

    # Obtener los datos de la vista
    datos = VistaCompraVenta.objects.all()

    # Cargar la plantilla HTML
    template = get_template('proveedor/reportes/reporte_compraVenta_pdf.html')
    context = {
        'datos': datos,
    }
    html = template.render(context)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="compra_venta.pdf"'

    # Convertir HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    
    return response

@login_required
def vista_proceso_ingreso_listar(request):
    datos = VistaProcesoIngreso.objects.all()
    return render(request, 'proveedor/reportes/vista_proceso_ingreso.html', {'datos': datos})

# Exportar a Excel
def exportar_proceso_ingreso_excel(request):
    from django.http import HttpResponse
    import pandas as pd

    # Obtener los datos de la vista
    datos = VistaProcesoIngreso.objects.all()

    # Crear un DataFrame de pandas
    data = {
        'Usuario Nombre': [dato.usuNombre for dato in datos],
        'ID Ingreso': [dato.ingresoId for dato in datos],
        'Valor': [dato.ingresoValor for dato in datos],
        'Nombre': [dato.nombre for dato in datos],
    }
    df = pd.DataFrame(data)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="proceso_ingreso.xlsx"'

    # Exportar a Excel
    df.to_excel(response, index=False)

    return response

# Exportar a PDF
def exportar_proceso_ingreso_pdf(request):
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa

    # Obtener los datos de la vista
    datos = VistaProcesoIngreso.objects.all()

    # Cargar la plantilla HTML
    template = get_template('proveedor/reportes/reporte_procesoIngreso_pdf.html')
    context = {
        'datos': datos,
    }
    html = template.render(context)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="proceso_ingreso.pdf"'

    # Convertir HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    
    return response

#----------------------------
#VISTA DE REGISTRO
#----------------------------

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # O a donde quieras redirigir después de registrar
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

#----------------------------
#VISTA DE PROVEEDOR
#-----------------------------

@login_required
def proveedor_listar(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor_listar')
    else:
        form = ProveedorForm()

    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/proveedor/proveedor.html', {
        'form': form,
        'proveedores': proveedores
    })
@login_required
@require_POST
def proveedor_eliminar(request, id):
    proveedor = get_object_or_404(Proveedor, proveedorNit=id)
    proveedor.delete()
    return redirect('proveedor_listar')

#----------------------------
#VISTA DE ROL
#-----------------------------


@login_required
def rol_listar(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()  # Ya no es necesario usar commit=False ni asignar usuario
            return redirect('rol_listar')
    else:
        form = RolForm()

    roles = Rol.objects.all()
    return render(request, 'proveedor/rol/rol.html', {
        'form': form,
        'roles': roles
    })

@login_required
@require_POST
def rol_eliminar(request, rolId):
    rol = get_object_or_404(Rol, rolId = rolId)
    rol.delete()
    return redirect('rol_listar')

#----------------------------
#VISTA DE CLIENTE
#-----------------------------

@login_required
def cliente_listar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente_obj = form.save(commit=False)
            cliente_obj.cliente = request.user
            cliente_obj.save()
            return redirect('cliente_listar')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'proveedor/cliente/cliente.html', {
        'form': form,
        'clientes': clientes
    })

@login_required
@require_POST
def cliente_eliminar(request, clienteCedula):
    cliente = get_object_or_404(Cliente, clienteCedula=clienteCedula)
    cliente.delete()
    return redirect('cliente_listar')

#----------------------------
#VISTA DE USUARIOS
#-----------------------------

@login_required
def usuario_listar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario_obj = form.save(commit=False)
            usuario_obj.usuario = request.user
            usuario_obj.save()
            return redirect('usuario_listar')
    else:
        form = UsuarioForm()

    usuarios = Usuario.objects.all()
    usuarios_django = User.objects.all()
    return render(request, 'proveedor/usuario/usuario.html', {
        'form': form,
        'usuarios': usuarios,
        'usuarios_django': usuarios_django
    })

@login_required
@require_POST
def usuario_eliminar(request, usuCedula):
    usuario = get_object_or_404(Usuario, usuCedula=usuCedula)
    usuario.delete()
    return redirect('usuario_listar')
    
#----------------------------
#VISTA DE INGRESO
#-----------------------------

@login_required
def ingreso_listar(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingreso_listar')
    else:
        form = IngresoForm()

    ingresos = Ingreso.objects.select_related('proveedorNit', 'usuCedula').all()
    # Usamos select_related para optimizar las consultas a la base de datos
    return render(request, 'proveedor/ingreso/ingreso.html', {
        'form': form,
        'ingresos': ingresos
    })

@login_required
@require_POST
def ingreso_eliminar(request, id):
    ingreso = get_object_or_404(Ingreso, ingresoId=id)
    ingreso.delete()
    return redirect('ingreso_listar')

def ingreso_editar(request, id):
    ingreso = get_object_or_404(Ingreso, ingresoId=id)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('ingreso_listar')
    else:
        form = IngresoForm(instance=ingreso)

    return render(request, 'proveedor/ingreso/ingreso.html', {
        'form': form,
        'ingreso': ingreso
    })

 # Exportar a Excel
def exportar_ingresos_excel(request):
    from django.http import HttpResponse
    import pandas as pd

    # Obtener los ingresos
    ingresos = Ingreso.objects.select_related('proveedorNit', 'usuCedula').all()

    # Crear un DataFrame de pandas
    data = {
        'ID': [ingreso.ingresoId for ingreso in ingresos],
        'Proveedor': [ingreso.proveedorNit.nombre for ingreso in ingresos],
        'Usuario': [ingreso.usuCedula.usuNombre for ingreso in ingresos],
        'Cantidad': [ingreso.ingresoCantidad for ingreso in ingresos],
        'Valor': [ingreso.ingresoValor for ingreso in ingresos],
    }
    df = pd.DataFrame(data)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ingresos.xlsx"'

    # Exportar a Excel
    df.to_excel(response, index=False)

    return response

 # Exportar a PDF
def exportar_ingresos_pdf(request):
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    # Obtener los ingresos
    ingresos = Ingreso.objects.select_related('proveedorNit', 'usuCedula').all()
    # Cargar la plantilla HTML
    template = get_template('proveedor/ingreso/ingreso_pdf.html')
    context = {
        'ingresos': ingresos,
        }
    html = template.render(context)
    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ingresos.pdf"'
    # Convertir HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    return response

#----------------------------
#VISTA DE PRODUCTO
#-----------------------------

from django.db import IntegrityError

@login_required
def producto_listar(request):
    from .forms import ProductoForm
    productos = Producto.objects.all()
    error_id = False
    success = False

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Producto guardado exitosamente.')
                form = ProductoForm()  # Limpia el formulario después de guardar
            except IntegrityError:
                error_id = True
        else:
            # Detecta si el error es por ID duplicado
            if 'productoId' in form.errors and any('already exists' in e for e in form.errors['productoId']):
                error_id = True
    else:
        form = ProductoForm()
    return render(request, 'proveedor/producto/producto.html', {
        'form': form,
        'productos': productos,
        'error_id': error_id,
        'success': success
    })
@login_required
@require_POST
def producto_eliminar(request, producto_id):
    producto = get_object_or_404(Producto, productoId=producto_id)
    producto.delete()
    return redirect('producto_listar')

#----------------------------
#VISTA DE VENTA
#-----------------------------

@login_required
def venta_listar(request):
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            venta_obj = form.save(commit=False)
            venta_obj.venta = request.user
            venta_obj.save()
            return redirect('venta_listar')
    else:
        form = VentaForm()

    ventas = Venta.objects.all()
    return render(request, 'proveedor/venta/venta.html', {
        'form': form,
        'ventas': ventas


    })

@login_required
@require_POST
def venta_eliminar(request, ventaId):
    venta = get_object_or_404(Venta, ventaId=ventaId)
    venta.delete()
    return redirect('venta_listar')

 # Exportar a Excel
def exportar_ventas_excel(request):
    from django.http import HttpResponse
    import pandas as pd

    # Obtener las ventas
    ventas = Venta.objects.select_related('productoId', 'clienteCedula', 'usuCedula').all()

    # Crear un DataFrame de pandas
    data = {
        'ID Venta': [venta.ventaId for venta in ventas],
        'Cantidad': [venta.ventaCantidad for venta in ventas],
        'Tipo Producto': [venta.ventaTipoProducto for venta in ventas],
        'Método de Pago': [venta.ventaMetodoPago for venta in ventas],
        'Precio Total': [venta.ventaPrecio for venta in ventas],
        'Producto': [str(venta.productoId) for venta in ventas],
        'Cliente': [str(venta.clienteCedula) for venta in ventas],
        'Usuario': [str(venta.usuCedula) for venta in ventas],
    }
    df = pd.DataFrame(data)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ventas.xlsx"'

    # Exportar a Excel
    df.to_excel(response, index=False)

    return response

 # Exportar a PDF
def exportar_ventas_pdf(request):
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa

    # Obtener las ventas
    ventas = Venta.objects.select_related('productoId', 'clienteCedula', 'usuCedula').all()

    # Cargar la plantilla HTML
    template = get_template('proveedor/venta/venta_pdf.html')
    context = {
        'ventas': ventas,
    }
    html = template.render(context)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ventas.pdf"'

    # Convertir HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    return response