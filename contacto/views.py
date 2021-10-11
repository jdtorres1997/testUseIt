from django.shortcuts import render, redirect
from .models import Contacto
from django.contrib.auth.decorators import login_required
from .forms import ContactoAddForm, ContactoEditForm
from django.contrib import messages
from empresaCliente.models import EmpresaCliente

# Create your views here.
@login_required
def gestion_contactos(request):
	# Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
	usuario = request.user
	return render(request, 'contacto/gestion.html',
					{'contactos': Contacto.get_contactos(usuario)})

@login_required
def add_contacto(request):
	usuario = request.user
	empresas_clientes_queryset = EmpresaCliente.get_empresas_clientes(usuario)
	if request.method == 'POST':
		form = ContactoAddForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Contacto registrado exitosamente')
			contacto = form.save(commit=False)
			contacto.propietario = usuario
			contacto.save()
			return redirect('contactos:gestion')
		else:
			form.listarEmpresasclientes(empresas_clientes_queryset)
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'contacto/add.html', {'form': form})
	else:
		form = ContactoAddForm()
		form.listarEmpresasclientes(empresas_clientes_queryset)
		return render(request, 'contacto/add.html',
					{'form': form})

@login_required
def editar_contacto(request, id_contacto):
	contacto = Contacto.objects.get(id=id_contacto)
	usuario = request.user
	if request.method == 'POST':
		form = ContactoEditForm(request.POST, instance=contacto)
		if form.is_valid():
			messages.success(request, 'Contacto registrado exitosamente')
			form.save()
			return redirect('contactos:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'contacto/edit.html', {'form': form})
	else:
		form = ContactoEditForm(instance=contacto)
		return render(request, 'contacto/edit.html',
					{'form': form})

@login_required
def eliminar_contacto(request, id_contacto):
	contacto = Contacto.objects.get(id=id_contacto)
	usuario = request.user

	if True:
		if request.method == 'POST':
			
			contacto.delete()
			messages.success(request, 'Has eliminado el contacto exitosamente!')
			return redirect('contactos:gestion')
		else:
			return render(request, 'contacto/delete.html', {'contacto': contacto})
	else:
		messages.error(request, 'No estas autorizado para realizar esta acción')
		return redirect('contactos:gestion')

@login_required
def detail_contacto(request, id_contacto):
	contacto = Contacto.objects.get(id=id_contacto)
	usuario = request.user

	return render(request, 'contacto/detail.html', {'contacto': contacto})