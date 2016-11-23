from django.db import models

from core.models import TimeStampedModel

class Produto(TimeStampedModel):
	nome = models.CharField(max_length=255)
	preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	def __str__(self):
		return self.nome
