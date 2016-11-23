from .models import Safra
from .serializer import SafraSerializer

from safras.models import Safra

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
        safra.atualizar_servicos()
        return Response({'message':'Serviços da safra atualizados com sucesso'})
