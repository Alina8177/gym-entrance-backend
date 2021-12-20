from rest_framework import serializers

from .models import Gym, Order, Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ("id", "name", "description", "is_archive", "created_at")


class GymSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True)
    class Meta:
        model = Gym
        fields = ("id", "name", "location", "zip_code", "programs")

class GymShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ("id", "name", "location", "zip_code", )

class OrderSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True)
    gym = GymShortSerializer()
    

    class Meta:
        model = Order
        fields = ("id", "uid", "status", "programs", "created_at", "updated_at","total", "valid_to", "gym")

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "uid", "programs", "gym")
        read_only_fields = ("id", "uid",)