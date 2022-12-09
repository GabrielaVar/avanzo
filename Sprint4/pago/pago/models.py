from django.db import models

class Pago(models.Model):
    valor = models.IntegerField(null=True, blank=True, default=None)
    descuento = models.FloatField(null=True, blank=True, default=None)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.valor)

# Create your models here.
