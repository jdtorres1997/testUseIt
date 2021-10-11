from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
#from django_select2.forms import Select2Widget
from .models import Empresa, UsuariosEmpresa
from django import forms 
import re

class EmpresaAddForm(ModelForm): 
    class Meta:
        model = Empresa
        fields = ('nit', 'nombre', 'nombre_comercial', 'direccion', 'telefono', 'email', 'sitio_web', 'pais', 'estado', 'ciudad')

class EmpresaEditForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ('nit', 'nombre', 'nombre_comercial', 'direccion', 'telefono', 'email', 'sitio_web', 'pais', 'estado', 'ciudad')

class VinculacionForm(ModelForm): 
    class Meta:
        model = UsuariosEmpresa
        fields = ('usuario_invitado',)
