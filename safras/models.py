from django.db import models
from django.db.models import Sum

from core.models import TimeStampedModel

class Safra(TimeStampedModel):
    nome = models.CharField(max_length=255)
    data_inicial = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return self.nome

    def atualizar_servicos(self):
        for servico in self.servicos.all():
            total = servico.servico_produto.aggregate(Sum('custo_total'))['custo_total__sum']
            servico.custo_total = total
            servico.save()