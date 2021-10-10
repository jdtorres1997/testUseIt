from django.shortcuts import render, redirect
from .models import EmpresaCliente
from django.contrib.auth.decorators import login_required
from .forms import EmpresaAddForm, EmpresaEditForm
from django.contrib import messages

# Create your views here.
@login_required
def gestion_empresas(request):
	# Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
	usuario = request.user
	return render(request, 'empresa_cliente/gestion.html',
					{'empresas': EmpresaCliente.get_info()})

@login_required
def add_empresa(request):
	usuario = request.user
	if request.method == 'POST':
		form = EmpresaAddForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Empresa registrado exitosamente')
			empresa = form.save(commit=False)
			empresa.propietario = usuario
			empresa.save()
			return redirect('empresas_clientes:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'empresa_cliente/add.html', {'form': form})
	else:
		form = EmpresaAddForm()
		return render(request, 'empresa_cliente/add.html',
					{'form': form})

@login_required
def editar_empresa(request, id_empresa):
	empresa = EmpresaCliente.objects.get(id=id_empresa)
	usuario = request.user
	print(empresa)
	if request.method == 'POST':
		form = EmpresaEditForm(request.POST, instance=empresa)
		if form.is_valid():
			messages.success(request, 'Empresa registrado exitosamente')
			form.save()
			return redirect('empresas_clientes:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'empresa_cliente/edit.html', {'form': form})
	else:
		form = EmpresaEditForm(instance=empresa)
		return render(request, 'empresa_cliente/edit.html',
					{'form': form})

@login_required
def eliminar_empresa(request, id_empresa):
	empresa = EmpresaCliente.objects.get(id=id_empresa)
	usuario = request.user

	if True:
		if request.method == 'POST':
			
			empresa.delete()
			messages.success(request, 'Has eliminado la empresa exitosamente!')
			return redirect('empresas_clientes:gestion')
		else:
			return render(request, 'empresa_cliente/delete.html', {'empresa': empresa})
	else:
		messages.error(request, 'No estas autorizado para realizar esta acción')
		return redirect('empresas_clientes:gestion')

@login_required
def detail_empresa(request, id_empresa):
	empresa = EmpresaCliente.objects.get(id=id_empresa)
	usuario = request.user

	return render(request, 'empresa_cliente/detail.html', {'empresa': empresa})