#coding: utf-8
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


helper_patterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),    
]

urlpatterns = helper_patterns
#It is only necessary the registration of the main route
urlpatterns.extend(router.urls)
