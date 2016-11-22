from django.db import models

from core.models import TimeStampedModel

class Servico(TimeStampedModel):
    nome = models.CharField(max_length=255)
    data_inicial = models.DateField()
    data_final = models.DateField()
    safra = models.ForeignKey('safras.Safra')
    produtos = models.ManyToManyField('produtos.Produto')
