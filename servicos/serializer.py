from .models import Servico, ServicoProduto
from rest_framework import serializers



class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servico
        fields = ['id','nome','data_inicial','data_final', 'safra','custo_total']

    def validate(self, data):
        if data['data_inicial'] > data['data_final']:
            raise serializers.ValidationError("Data final não pode ser maior que a final")
        return data

class ServicoProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicoProduto
        fields = ['id', 'quantidade', 'produto','servico']