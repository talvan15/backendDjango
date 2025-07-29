from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Aluno, Presenca
from .serializers import AlunoSerializer, PresencaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer