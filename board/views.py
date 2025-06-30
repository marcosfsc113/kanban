from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status#importar viewset para nao ser necessario fazer o CRUD na mao
from .models import Bucket, Card
from django.shortcuts import render
from .serializers import BucketSerializer, CardSerializer

class BucketViewSet(viewsets.ModelViewSet):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardUpdateStatusView(APIView):
    def patch(self, request, pk, format=None):
        card = Card.objects.get(pk=pk)
        new_bucket_id = request.data.get('bucket_id')
        new_bucket = Bucket.objects.get(pk=new_bucket_id)
        
        card.bucket = new_bucket

        card.save() 

        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardDetailView(APIView):
    def get(self, request, pk, format=None):

        try:
            card = Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            return Response(
                {'error': 'Paciente não encontrado.'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)

def home_view(request):
    buckets = Bucket.objects.all()
    context = {
        'buckets': buckets,
    }
    return render(request, 'board/home.html', context)

