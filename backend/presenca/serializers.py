from rest_framework import serializers
from .models import Aluno, Presenca

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    presencas = PresencaSerializer(many=True, read_only=True)
    class Meta:
        model = Aluno
        fields = '__all__'