from rest_framework import permissions, viewsets, mixins

from apps.gym.models import Gym
from apps.gym.serializers import GymSerializer

# Create your views here.
class GymViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = GymSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Gym.objects.all()