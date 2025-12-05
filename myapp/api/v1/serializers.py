from rest_framework import serializers

from django.contrib.auth import get_user_model
from myapp.models import PlanoTreino, PlanoDieta

Usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class PlanoTreinoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    exercicios_display = serializers.CharField(source="get_exercicios_display", read_only=True)

    class Meta:
        model = PlanoTreino
        fields = '__all__'

class PlanoDietaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = PlanoDieta
        fields = '__all__'