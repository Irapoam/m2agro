from .models import Servico, ServicoProduto
from .serializer import ServicoSerializer, ServicoProdutoSerializer

from rest_framework.viewsets import ModelViewSet

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoProdutoViewSet(ModelViewSet):
    queryset = ServicoProduto.objects.all()
    serializer_class = ServicoProdutoSerializer
