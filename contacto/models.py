from django.db import models

from django.conf import settings
from empresaCliente.models import EmpresaCliente
from empresa.models import Empresa,UsuariosEmpresa
from django.db.models import Q

class Contacto(models.Model):
    nombres = models.CharField(verbose_name='Nombres',max_length=100)
    apellidos = models.CharField(verbose_name='Apellidos',max_length=100)
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    celular = models.BigIntegerField(verbose_name='Celular')
    email = models.EmailField(verbose_name='Correo electrónico')
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Propietario')
    empresa_cliente = models.ForeignKey(EmpresaCliente, on_delete=models.CASCADE, verbose_name='Empresa cliente')

    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)

    def get_info():
        contactos = Contacto.objects.order_by('id')
        return contactos

    def get_contactos(usuario):

        usuarios_empresa = UsuariosEmpresa.objects.filter(usuario_invitado=usuario).values_list('empresa', flat=True).distinct()
        contactos = Contacto.objects.filter(Q(empresa_cliente__empresa__id__in=usuarios_empresa) | Q(empresa_cliente__empresa__propietario=usuario)).order_by('id')
        return contactos

    def get_contactos_empresa_cliente(empresa_cliente):
        empresa_clientes = Contacto.objects.filter(empresa_cliente=empresa_cliente).order_by('id')
        return empresa_clientes