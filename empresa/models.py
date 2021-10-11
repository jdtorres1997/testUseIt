from django.db import models
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.models import User

class Empresa(models.Model):
    nit = models.CharField(verbose_name='NIT',max_length=20)
    nombre = models.CharField(verbose_name='Nombre de la empresa',max_length=100)
    nombre_comercial = models.CharField(verbose_name='Nombre comercial de la empresa',max_length=100)
    direccion = models.CharField(verbose_name='Dirección',max_length=100)
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Correo electrónico')
    sitio_web = models.URLField(max_length=200, verbose_name='Sitio Web')
    pais = models.CharField(verbose_name='País',max_length=100)
    estado = models.CharField(verbose_name='Departamento',max_length=100)
    ciudad = models.CharField(verbose_name='Ciudad',max_length=100)
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Propietario')

    def __str__(self):
        return "%s - %s" % (self.nit, self.nombre_comercial)
    
    def get_info():
        empresas = Empresa.objects.order_by('id')
        return empresas

    def get_empresas(usuario):
        try:
            usuarios_empresa = UsuariosEmpresa.objects.filter(usuario_invitado=usuario).values_list('empresa', flat=True).distinct()
            empresas = Empresa.objects.filter(Q(id__in=usuarios_empresa) | Q(propietario=usuario)).order_by('id')
            return empresas
        except:
            return None

class UsuariosEmpresa(models.Model):
    usuario_invitado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    def get_usuarios_invitados(empresa):
        try:
            usuarios_empresa = UsuariosEmpresa.objects.filter(empresa=empresa).values_list('usuario_invitado', flat=True).distinct()
            usuarios = User.objects.filter(id__in=usuarios_empresa).order_by('id')
            return usuarios
        except:
            return None