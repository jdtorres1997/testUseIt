from django.shortcuts import render, redirect
from .models import EmpresaCliente
from django.contrib.auth.decorators import login_required
from .forms import EmpresaAddForm, EmpresaEditForm
from django.contrib import messages
from contacto.models import Contacto
from oportunidad.models import Oportunidad
from empresa.models import Empresa
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EmpresaClienteSerializer

# Create your views here.
@login_required
def gestion_empresas(request):
	# Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
	usuario = request.user
	return render(request, 'empresa_cliente/gestion.html',
					{'empresas': EmpresaCliente.get_empresas_clientes(usuario)})

@login_required
def add_empresa(request):
	usuario = request.user
	empresas_queryset = Empresa.get_empresas(usuario)
	if request.method == 'POST':
		form = EmpresaAddForm(request.POST)
		if form.is_valid():
			empresa = form.save(commit=False)
			empresa.propietario = usuario
			empresa.save()
			messages.success(request, 'Empresa cliente registrada exitosamente')
			return redirect('empresas_clientes:gestion')
		else:
			form.listarEmpresas(empresas_queryset)
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'empresa_cliente/add.html', {'form': form})
	else:
		form = EmpresaAddForm()
		form.listarEmpresas(empresas_queryset)
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
			form.save()
			messages.success(request, 'Empresa cliente registrada exitosamente')
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
			messages.success(request, 'Has eliminado la empresa cliente exitosamente!')
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
	contactos = Contacto.get_contactos_empresa_cliente(empresa)
	oportunidades = Oportunidad.get_oportunidades_empresa_cliente(empresa, usuario)
	return render(request, 'empresa_cliente/detail.html', {'empresa': empresa, 'contactos': contactos, 'oportunidades':oportunidades})

class EmpresaClienteViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows EmpresaCliente to be viewed or edited.
	"""	
	serializer_class = EmpresaClienteSerializer
	permission_classes = [permissions.IsAuthenticated]
	queryset = EmpresaCliente.get_info()

	def get_queryset(self):
		user = self.request.user
		queryset = EmpresaCliente.get_empresas_clientes(user)
		return queryset
