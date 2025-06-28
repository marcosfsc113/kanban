from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import BucketViewSet, CardViewSet

router = DefaultRouter() #Gera rotas automaticamente
router.register(r'buckets', BucketViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [

    path('', include(router.urls)), #Junta as rotas geradas dentro do app
]