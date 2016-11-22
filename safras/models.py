from django.db import models

from core.models import TimeStampedModel

class Safra(TimeStampedModel):
    nome = models.CharField(max_length=255)
    data_inicial = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return self.nome
