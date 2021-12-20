from rest_framework import mixins, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PaymentCreateSerializer, PaymentSerializer, UserRegisterSerializer, UserSerializer
from .models import Payment, PaymentStatus, User


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserRegisterSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = User.objects.all()

    def get_instance(self):
        return self.request.user

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if self.action == "retrieve" and not user.is_staff:
            queryset = queryset.filter(pk=user.pk)
        return queryset

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ["update", "me", "partial_update"]:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action in ["create"]:
            serializer_class = UserRegisterSerializer
        else:
            serializer_class = UserSerializer
        return serializer_class

    @action(["get", "put", "patch"], detail=False)
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        if request.method == "GET":
            self.action = "retrieve"
            return self.retrieve(request, *args, **kwargs)
        elif request.method == "PUT":
            self.action = "update"
            return self.update(request, *args, **kwargs)
        elif request.method == "PATCH":
            self.action = "partial_update"
            return self.partial_update(request, *args, **kwargs)
    

class PaymentViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Payment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

    def get_serializer_class(self):
        if self.action in ['create']:
            self.serializer_class = PaymentCreateSerializer
        else:
            self.serializer_class = PaymentSerializer
        return super().get_serializer_class()
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, *args, **kwargs):
        payment = self.get_object()
        if payment.status == PaymentStatus.CANCELED:
            return Response({'code': 'error', 'msg': 'This payment has successfully canceled before'}, status=status.HTTP_400_BAD_REQUEST)
        payment.status = PaymentStatus.CANCELED
        payment.save()
        return Response(PaymentSerializer(payment).data)