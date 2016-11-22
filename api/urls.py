#coding: utf-8
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from produtos.views import ProdutoViewSet
from safras.views import SafraViewSet
from servicos.views import ServicoViewSet, ServicoProdutoViewSet

router = DefaultRouter()

helper_patterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),    
]

router.register(r'produtos', ProdutoViewSet)
router.register(r'safras', SafraViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'servicos-e-produtos', ServicoProdutoViewSet)

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
