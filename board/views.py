from rest_framework import viewsets #importar viewset para nao ser necessario fazer o CRUD na mao
from .models import Bucket, Card
from .serializers import BucketSerializer, CardSerializer

class BucketViewSet(viewsets.ModelViewSet):
    #ModelCiewSet relaciona os modelos com as rotas
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer