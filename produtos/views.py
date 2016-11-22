
from .models import Produto
from .serializer import ProdutoSerializer
from safras.models import Safra
from servicos.models import Servico, ServicoProduto


from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class AtualizarProdutos(APIView):
    
    def get(self, request, safra_id):
        safra = Safra.objects.get(id=safra_id)
        servicos = Servico.objects.filter(safra=safra)
        
        