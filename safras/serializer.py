# coding: utf-8

from rest_framework import serializers
from .models import Safra


class SafraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Safra
        fields = ['id','nome','data_inicial','data_final']
        

    def validate(self, data):
        if data['data_inicial'] > data['data_final']:
            raise serializers.ValidationError("Data final não pode ser maior que a final")
        return data