from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from .models import Charge, Payment, User


class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ("id", "email", "balance")

class UserSetPasswordSerializer(serializers.Serializer):
    default_error_messages = {"password_mismatch": "Password mismatch"}
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    re_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    def validate(self, attrs):
        re_password = attrs.pop("re_password")

        if attrs["password"] == re_password:
            try:
                validate_password(re_password)
            except django_exceptions.ValidationError as e:
                serializer_error = serializers.as_serializer_error(e)
                raise serializers.ValidationError(
                    {"password": serializer_error["non_field_errors"]}
                )

            return attrs
        else:
            self.fail("password_mismatch")


class UserRegisterSerializer(UserSetPasswordSerializer, serializers.ModelSerializer):
    default_error_messages = {"cannot_create_user": "User is already exists"}

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "re_password",
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        password_validation = super().validate(attrs=attrs)
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
        return user


class PaymentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Payment
        fields = ("id", "total", "user")

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id", "total", "created_at", "updated_at", "status",)

class ChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charge
        fields = ("id", "order", "status", "created_at", "updated_at")