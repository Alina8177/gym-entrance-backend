from rest_framework import permissions, viewsets, mixins

from apps.gym.models import Gym, Order
from apps.gym.serializers import GymSerializer, OrderSerializer

# Create your views here.
class GymViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = GymSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Gym.objects.all()


class OrderViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(order_by=user)
        return queryset