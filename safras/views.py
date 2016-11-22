from .models import Safra
from .serializer import SafraSerializer

from rest_framework.viewsets import ModelViewSet

class SafraViewSet(ModelViewSet):
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer

