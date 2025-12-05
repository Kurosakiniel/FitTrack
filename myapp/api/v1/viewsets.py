from rest_framework import viewsets, permissions, filters
from django.contrib.auth import get_user_model
from myapp.models import PlanoTreino, PlanoDieta

from myapp.api.v1.serializers import (

    UsuarioSerializer,
    PlanoTreinoSerializer,
    PlanoDietaSerializer,
)

Usuario = get_user_model()

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(is_active=True)
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "email"]

class PlanoTreinoViewSet(viewsets.ModelViewSet):
    queryset = PlanoTreino.objects.filter(is_active=True)
    serializer_class = PlanoTreinoSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome", "descricao", "exercicios"]

    def perform_destroy(self, instance):
        instance.delete() 

class PlanoDietaViewSet(viewsets.ModelViewSet):
    queryset = PlanoDieta.objects.filter(is_active=True)
    serializer_class = PlanoDietaSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["restricoes", "refeicoes"]

    def perform_destroy(self, instance):
        instance.delete()