from django.db import models
from django.conf import settings
from empresaCliente.models import EmpresaCliente
from contacto.models import Contacto
from empresa.models import Empresa,UsuariosEmpresa
from django.db.models import Q

ESTADO_CHOICES = (
    ("En proceso", "En proceso"),
    ("Ganada", "Ganada"),
    ("No ganada", "No ganada"),
    ("Cancelada", "Cancelada (Descartada)"),
)

class Oportunidad(models.Model):
    UUID = models.CharField(verbose_name='UUID',max_length=100)
    consecutivo = models.IntegerField(verbose_name='Consecutivo', default=0)
    nombre = models.CharField(verbose_name='Nombre de la oportunidad de negocio',max_length=100)
    monto = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Monto total de la oportunidad')
    estado = models.CharField(verbose_name='Estado',max_length=100, choices = ESTADO_CHOICES, default='en_proceso')
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Propietario')
    empresa_cliente = models.ForeignKey(EmpresaCliente, on_delete=models.CASCADE, verbose_name='Empresa cliente')
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, verbose_name='Contacto')

    def __str__(self):
        return "%s - %s" % (self.UUID, self.nombre)

    def get_info():
        oportunidades = Oportunidad.objects.order_by('id')
        return oportunidades

    def get_oportunidades(usuario):
        oportunidades = Oportunidad.objects.filter(Q(propietario=usuario) | Q(empresa_cliente__empresa__propietario=usuario)).order_by('id')
        return oportunidades

    def get_oportunidades_empresa_cliente(empresa_cliente, usuario):
        oportunidades = Oportunidad.objects.filter(Q(propietario=usuario) | Q(empresa_cliente__empresa__propietario=usuario)).filter(empresa_cliente=empresa_cliente).order_by('id')
        return oportunidades

    def save(self, *args, **kwargs):
        uuid = ''
        if self.empresa_cliente:
            ultima_oportunidad = Oportunidad.objects.filter(empresa_cliente=self.empresa_cliente).order_by('consecutivo').last()
            siguiente_consecutivo = ultima_oportunidad.consecutivo if ultima_oportunidad else 0
            siguiente_consecutivo = siguiente_consecutivo + 1
            uuid = 'OPO-'+ self.empresa_cliente.nit + '-' + str(siguiente_consecutivo)
            self.consecutivo = siguiente_consecutivo
        self.UUID = uuid
        super(Oportunidad, self).save(*args, **kwargs)