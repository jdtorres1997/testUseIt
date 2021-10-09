from django.db import models

from django.conf import settings
from empresaCliente.models import EmpresaCliente

class Contacto(models.Model):
    nombres = models.CharField(verbose_name='Nombres',max_length=100)
    apellidos = models.CharField(verbose_name='Apellidos',max_length=100)
    telefono = models.PositiveIntegerField(verbose_name='Teléfono')
    celular = models.PositiveIntegerField(verbose_name='Celular')
    email = models.EmailField(verbose_name='Correo electrónico')
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    empresa_cliente = models.ForeignKey(EmpresaCliente, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)
