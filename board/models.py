from django.db import models

class Bucket(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome #Como o card vai aparecer?

class Card(models.Model):
    nome_paciente = models.CharField(max_length=100)
    data_admissao = models.DateField()
    estado_civil = models.CharField(max_length=30)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return f"{self.nome_paciente} ({self.bucket.nome})" #Exibicao do nome juntamente com a etapa do paciente