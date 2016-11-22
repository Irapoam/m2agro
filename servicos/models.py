from django.db import models

from core.models import TimeStampedModel

class Servico(TimeStampedModel):
    nome = models.CharField(max_length=255)
    data_inicial = models.DateField()
    data_final = models.DateField()
    safra = models.ForeignKey('safras.Safra')
    produtos = models.ManyToManyField('produtos.Produto', through='ServicoProduto')
    custo_total = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.nome


class ServicoProduto(models.Model):
    quantidade = models.IntegerField(default=0)
    servico = models.ForeignKey('servicos.Servico')
    produto = models.ForeignKey('produtos.Produto')
