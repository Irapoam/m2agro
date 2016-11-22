from .models import Produto
from .serializer import ProdutoSerializer

from rest_framework.viewsets import ModelViewSet

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

