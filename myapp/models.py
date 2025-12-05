from django.contrib.auth.models import AbstractUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def delete(self):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True
        
class Usuario(AbstractUser, LoginRequiredMixin):
    peso_atual = models.FloatField(null=True)
    altura = models.FloatField(null=True)

class PlanoTreino(BaseModel, LoginRequiredMixin):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Exercicios(models.TextChoices):
        SUPINO = "SUPINO", "Supino"
        AGACHAMENTO = "AGACHAMENTO", "Agachamento"
        ABDOMINAL = "ABDOMINAL", "Abdominal"
        CORRIDA = "CORRIDA", "Corrida"

    exercicios = models.CharField(
        max_length=50,
        choices=Exercicios.choices
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="treinos")

class PlanoDieta(BaseModel, LoginRequiredMixin):
    calorias_por_dia = models.IntegerField()
    refeicoes = models.TextField()
    restricoes = models.TextField(blank=True)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="dietas")

