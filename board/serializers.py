from rest_framework import serializers #Importar para conversao de dados em JSON
from .models import Bucket, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class BucketSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Bucket
        fields = ['id', 'nome', 'cards']
