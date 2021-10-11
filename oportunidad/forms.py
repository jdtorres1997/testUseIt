from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
#from django_select2.forms import Select2Widget
from .models import Oportunidad
from django import forms 
import re

class OportunidadAddForm(ModelForm): 
    def listarEmpresasclientes(self, empresas_queryset):
        self.fields['empresa_cliente'].queryset = empresas_queryset
    
    def listarContactos(self, contactos_queryset):
        self.fields['contacto'].queryset = contactos_queryset

    class Meta:
        model = Oportunidad
        fields = ('nombre', 'monto', 'estado', 'contacto', 'empresa_cliente')

class OportunidadEditForm(ModelForm):
    
    def listarContactos(self, contactos_queryset):
        self.fields['contacto'].queryset = contactos_queryset

    class Meta:
        model = Oportunidad
        fields = ('nombre', 'monto', 'estado', 'contacto')
