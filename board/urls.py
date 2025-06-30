from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import BucketViewSet, CardViewSet, CardUpdateStatusView, CardDetailView, home_view
router = DefaultRouter() #Gera rotas automaticamente
router.register(r'buckets', BucketViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    path('', include(router.urls)), #Junta as rotas geradas dentro do app
    path('cards/<int:pk>/update_status/', CardUpdateStatusView.as_view(), name='card-update-status'),
    path('cards/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
]