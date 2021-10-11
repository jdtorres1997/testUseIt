from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
#from django_select2.forms import Select2Widget
from .models import EmpresaCliente
from django import forms 
import re

class EmpresaAddForm(ModelForm): 
    def listarEmpresas(self, empresas_queryset):
        self.fields['empresa'].queryset = empresas_queryset

    class Meta:
        model = EmpresaCliente
        fields = ('nit', 'nombre', 'nombre_comercial', 'direccion', 'telefono', 'email', 'sitio_web', 'pais', 'estado', 'ciudad','empresa')


class EmpresaEditForm(ModelForm):
    class Meta:
        model = EmpresaCliente
        fields = ('nit', 'nombre', 'nombre_comercial', 'direccion', 'telefono', 'email', 'sitio_web', 'pais', 'estado', 'ciudad')
