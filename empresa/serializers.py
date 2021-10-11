from .models import Empresa, UsuariosEmpresa
from rest_framework import serializers


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = ['url', 'nit', 'nombre', 'nombre_comercial', 'direccion', 'telefono', 'email', 'sitio_web', 'pais', 'estado', 'ciudad']


class UsuariosEmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsuariosEmpresa
        fields = ['url', 'usuario_invitado', 'empresa']