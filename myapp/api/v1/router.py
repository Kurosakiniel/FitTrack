from rest_framework.routers import DefaultRouter
from .viewsets import UsuarioViewSet
from .viewsets import PlanoTreinoViewSet
from .viewsets import PlanoDietaViewSet

router = DefaultRouter()
router.register("usuarios", UsuarioViewSet)
router.register("treinos", PlanoTreinoViewSet)
router.register("dietas", PlanoDietaViewSet)

urlpatterns = router.urls
