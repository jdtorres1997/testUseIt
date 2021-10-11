from django.shortcuts import render, redirect
from .models import Empresa, UsuariosEmpresa
from django.contrib.auth.decorators import login_required
from .forms import EmpresaAddForm, EmpresaEditForm, VinculacionForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required
def gestion_empresas(request):
	# Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
	usuario = request.user
	return render(request, 'empresa/gestion.html',
					{'empresas': Empresa.get_empresas(usuario)})

@login_required
def add_empresa(request):
	usuario = request.user
	if request.method == 'POST':
		form = EmpresaAddForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Empresa registrada exitosamente')
			empresa = form.save(commit=False)
			empresa.propietario = usuario
			empresa.save()
			return redirect('empresa:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'empresa/add.html', {'form': form})
	else:
		form = EmpresaAddForm()
		return render(request, 'empresa/add.html',
					{'form': form})

@login_required
def editar_empresa(request, id_empresa):
	empresa = Empresa.objects.get(id=id_empresa)
	usuario = request.user
	if request.method == 'POST':
		form = EmpresaEditForm(request.POST, instance=empresa)
		if form.is_valid():
			messages.success(request, 'Empresa registrada exitosamente')
			form.save()
			return redirect('empresa:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'empresa/edit.html', {'form': form})
	else:
		form = EmpresaEditForm(instance=empresa)
		return render(request, 'empresa/edit.html',
					{'form': form})

@login_required
def eliminar_empresa(request, id_empresa):
	empresa = Empresa.objects.get(id=id_empresa)
	usuario = request.user

	if True:
		if request.method == 'POST':
			
			empresa.delete()
			messages.success(request, 'Has eliminado la empresa exitosamente!')
			return redirect('empresa:gestion')
		else:
			return render(request, 'empresa/delete.html', {'empresa': empresa})
	else:
		messages.error(request, 'No estas autorizado para realizar esta acción')
		return redirect('empresa:gestion')

@login_required
def detail_empresa(request, id_empresa):
	empresa = Empresa.objects.get(id=id_empresa)
	usuario = request.user
	usuarios_invitados = UsuariosEmpresa.get_usuarios_invitados(empresa)
	return render(request, 'empresa/detail.html', {'empresa': empresa, 'usuarios_invitados':usuarios_invitados})

@login_required
def eliminar_usuario(request, id_empresa, id_usuario):
	usuario = request.user
	empresa = Empresa.objects.get(id=id_empresa)
	usuario_invitado = User.objects.get(id=id_usuario)
	if empresa.propietario == usuario or usuario.is_superuser:
		UsuariosEmpresa.objects.filter(usuario_invitado=usuario_invitado).filter(empresa=empresa).delete()
		messages.success(request, 'Se ha desvinculado el usuario correctamente')
		return redirect('/empresas/detail/'+str(id_empresa))
	else:
		messages.error(request, 'No estas autorizado para realizar esta acción')
		return redirect('empresa:gestion')

@login_required
def vincular_usuario(request, id_empresa):
	usuario = request.user
	empresa = Empresa.objects.get(id=id_empresa)
	if empresa.propietario == usuario or usuario.is_superuser:
		if request.method == 'POST':
			form = VinculacionForm(request.POST)
			if form.is_valid():
				usuarios_empresa = form.save(commit=False)
				usuarios_empresa.empresa = empresa
				usuarios_empresa.save()
				messages.success(request, 'Se ha vinculado el usuario correctamente')
				return redirect('/empresas/detail/'+str(id_empresa))
			else:
				messages.error(request, 'Por favor corrige los errores')
				return render(request, 'empresa/vincular.html', {'form': form, 'empresa': empresa})
		else:
			form = VinculacionForm()
			return render(request, 'empresa/vincular.html',
						{'form': form, 'empresa': empresa})
	else:
		messages.error(request, 'No estas autorizado para realizar esta acción')
		return redirect('empresa:gestion')