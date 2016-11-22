# coding: utf-8

from rest_framework import serializers
from .models import Servico


class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servico
        fields = ['id','nome','data_inicial','data_final', 'safra','produtos']
        