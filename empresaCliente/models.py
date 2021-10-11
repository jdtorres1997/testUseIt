from django.db import models
from django.conf import settings
from empresa.models import Empresa,UsuariosEmpresa
from django.db.models import Q

class EmpresaCliente(models.Model):
    nit = models.CharField(verbose_name='NIT',max_length=20)
    nombre = models.CharField(verbose_name='Nombre de la empresa',max_length=100)
    nombre_comercial = models.CharField(verbose_name='Nombre comercial de la empresa',max_length=100)
    direccion = models.CharField(verbose_name='Dirección',max_length=100)
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Correo electrónico')
    sitio_web = models.URLField(max_length=200)
    pais = models.CharField(verbose_name='País',max_length=100)
    estado = models.CharField(verbose_name='Departamento',max_length=100)
    ciudad = models.CharField(verbose_name='Ciudad',max_length=100)
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Propietario')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
        return "%s - %s" % (self.nit, self.nombre_comercial)

    def get_info():
        empresas = EmpresaCliente.objects.order_by('id')
        return empresas

    def get_empresas_clientes(usuario):

        usuarios_empresa = UsuariosEmpresa.objects.filter(usuario_invitado=usuario).values_list('empresa', flat=True).distinct()
        empresas = EmpresaCliente.objects.filter(Q(empresa__id__in=usuarios_empresa) | Q(empresa__propietario=usuario)).order_by('id')
        return empresas

    def get_empresas_clientes_empresa(empresa):
        empresas = EmpresaCliente.objects.filter(empresa=empresa).order_by('id')
        return empresas