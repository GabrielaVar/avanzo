from django.db import models


class Solicitante(models.Model):
    pago = models.IntegerField(null=False, default=None)
    empresa = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.empresa)

# Create your models here.
