from .models import Safra
from .serializer import SafraSerializer

from safras.models import Safra
from servicos.models import Servico, ServicoProduto

from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class SafraViewSet(ModelViewSet):
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer


    @detail_route()
    def atualizar_servicos(self, request, pk):
        safra = self.get_object()
        servicos = Servico.objects.filter(safra=safra)

        for servico in servicos:
            total = 0
            for servico_produto in servico.servico_produto.all():
                total += servico_produto.quantidade * servico_produto.produto.preco
            servico.custo_total = total
            servico.save()

        return Response({'message':'Serviços da safra atualizados com sucesso'})
