from .models import Oportunidad
from rest_framework import serializers


class OportunidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oportunidad
        fields = ['url', 'nombre', 'monto', 'estado', 'contacto', 'empresa_cliente']
