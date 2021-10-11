from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
#from django_select2.forms import Select2Widget
from .models import Contacto
from django import forms 
import re

class ContactoAddForm(ModelForm): 
    def listarEmpresasclientes(self, empresas_queryset):
        self.fields['empresa_cliente'].queryset = empresas_queryset

    class Meta:
        model = Contacto
        fields = ('nombres', 'apellidos', 'telefono', 'celular', 'email', 'empresa_cliente')

class ContactoEditForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombres', 'apellidos', 'telefono', 'celular', 'email')