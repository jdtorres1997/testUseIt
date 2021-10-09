from django.db import models
from django.conf import settings
from empresaCliente.models import EmpresaCliente
from contacto.models import Contacto

ESTADO_CHOICES = (
    ("en_proceso", "En proceso"),
    ("ganada", "Ganada"),
    ("no_ganada", "No ganada"),
    ("cancelada", "Cancelada (Descartada)"),
)

class Oportunidad(models.Model):
    UUID = models.CharField(verbose_name='UUID',max_length=100)
    nombre = models.CharField(verbose_name='Nombre de la oportunidad de negocio',max_length=100)
    monto = models.PositiveIntegerField(verbose_name='Monto total de la oportunidad')
    estado = models.CharField(verbose_name='Estado',max_length=100, choices = ESTADO_CHOICES, default='en_proceso')
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    empresa_cliente = models.ForeignKey(EmpresaCliente, on_delete=models.CASCADE)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.UUID, self.nombre)
