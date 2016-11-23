
from django.db.models import Sum

from .models import Produto
from .serializer import ProdutoSerializer
from safras.models import Safra
from servicos.models import Servico, ServicoProduto


from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class AtualizarProdutos(APIView):
    
    def get(self, request, safra_id):
        safra = Safra.objects.get(id=safra_id)
        servicos = Servico.objects.filter(safra=safra)

        for servico in servicos:
            total = 0
            for servico_produto in servico.servico_produto.all():
                total += servico_produto.quantidade * servico_produto.produto.preco
            servico.custo_total = total
            servico.save()

        return Response({'message':'Servicos atualizados com sucesso'})
        