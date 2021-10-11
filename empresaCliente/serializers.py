from .models import EmpresaCliente
from rest_framework import serializers


class EmpresaClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmpresaCliente
        fields = ['url', 'nit', 'nombre', 'nombre_comercial', 'direccion', 'telefono', 'email', 'sitio_web', 'pais', 'estado', 'ciudad','empresa']
