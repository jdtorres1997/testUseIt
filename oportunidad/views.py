from django.shortcuts import render, redirect
from .models import Oportunidad
from django.contrib.auth.decorators import login_required
from .forms import OportunidadAddForm, OportunidadEditForm
from django.contrib import messages
from empresaCliente.models import EmpresaCliente
from contacto.models import Contacto

# Create your views here.
@login_required
def gestion_oportunidades(request):
	# Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
	usuario = request.user
	return render(request, 'oportunidad/gestion.html',
					{'oportunidades': Oportunidad.get_oportunidades(usuario)})

@login_required
def add_oportunidad(request):
	usuario = request.user
	empresas_clientes_queryset = EmpresaCliente.get_empresas_clientes(usuario)
	contactos_queryset = Contacto.get_contactos(usuario)
	if request.method == 'POST':
		form = OportunidadAddForm(request.POST)
		if form.is_valid():
			oportunidad = form.save(commit=False)
			oportunidad.propietario = usuario
			oportunidad.save()
			messages.success(request, 'Oportunidad registrada exitosamente')
			return redirect('oportunidades:gestion')
		else:
			form.listarEmpresasclientes(empresas_clientes_queryset)
			form.listarContactos(contactos_queryset)
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'oportunidad/add.html', {'form': form})
	else:
		form = OportunidadAddForm()
		form.listarEmpresasclientes(empresas_clientes_queryset)
		form.listarContactos(contactos_queryset)
		return render(request, 'oportunidad/add.html',
					{'form': form})

@login_required
def editar_oportunidad(request, id_oportunidad):
	oportunidad = Oportunidad.objects.get(id=id_oportunidad)
	usuario = request.user
	if request.method == 'POST':
		form = OportunidadEditForm(request.POST, instance=oportunidad)
		if form.is_valid():
			form.save()
			messages.success(request, 'Oportunidad registrada exitosamente')
			return redirect('oportunidades:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'oportunidad/edit.html', {'form': form})
	else:
		form = OportunidadEditForm(instance=oportunidad)
		return render(request, 'oportunidad/edit.html',
					{'form': form})

@login_required
def eliminar_oportunidad(request, id_oportunidad):
	oportunidad = Oportunidad.objects.get(id=id_oportunidad)
	usuario = request.user

	if True:
		if request.method == 'POST':
			
			oportunidad.delete()
			messages.success(request, 'Has eliminado la oportunidad exitosamente!')
			return redirect('oportunidades:gestion')
		else:
			return render(request, 'oportunidad/delete.html', {'oportunidad': oportunidad})
	else:
		messages.error(request, 'No estas autorizado para realizar esta acción')
		return redirect('oportunidades:gestion')

@login_required
def detail_oportunidad(request, id_oportunidad):
	oportunidad = Oportunidad.objects.get(id=id_oportunidad)
	usuario = request.user

	return render(request, 'oportunidad/detail.html', {'oportunidad': oportunidad})