from .models import Contacto
from rest_framework import serializers


class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = ['url', 'nombres', 'apellidos', 'telefono', 'celular', 'email', 'empresa_cliente']
