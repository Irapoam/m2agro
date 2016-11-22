from .models import Servico
from .serializer import ServicoSerializer

from rest_framework.viewsets import ModelViewSet

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

