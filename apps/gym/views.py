from django.utils import timezone

from datetime import timedelta
from rest_framework import permissions, status, viewsets, mixins
from rest_framework.response import Response

from apps.gym.models import Gym, Order
from apps.gym.serializers import GymSerializer, OrderCreateSerializer, OrderSerializer
from apps.authentication.models import Charge

# Create your views here.
class GymViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = GymSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Gym.objects.all()


class OrderViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(order_by=user)
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['list']:
            self.serializer_class = OrderSerializer
        else:
            self.serializer_class = OrderCreateSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order()
        order.order_by = user
        
        order.gym = serializer.validated_data['gym']
        order.total = 10
        order.valid_to = timezone.now() + timedelta(30)
        order.save()
        order.programs.set(serializer.validated_data['programs'])
        charge = Charge.objects.create(order=order, user=user)
        user.balance -= order.total
        user.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)