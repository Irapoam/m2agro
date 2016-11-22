# coding: utf-8

from rest_framework import serializers
from .models import Safra


class SafraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Safra
        fields = ['id','nome','data_inicial','data_final']
        