from django.db import models

from core.models import TimeStampedModel

class Servico(TimeStampedModel):
    nome = models.CharField(max_length=255)
    data_inicial = models.DateField()
    data_final = models.DateField()
    safra = models.ForeignKey('safras.Safra', related_name='servicos')
    produtos = models.ManyToManyField('produtos.Produto', through='ServicoProduto')
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nome


class ServicoProduto(models.Model):
    quantidade = models.IntegerField(default=0)
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    servico = models.ForeignKey('servicos.Servico', related_name='servico_produto')
    produto = models.ForeignKey('produtos.Produto', related_name='servico_produto')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.custo_total = self.quantidade*self.produto.preco
        super(ServicoProduto, self).save(force_insert=False, 
            force_update=False, using=None, update_fields=None)