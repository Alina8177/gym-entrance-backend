from rest_framework import serializers

from .models import Gym, Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ("id", "name", "description", "is_archive", "created_at")


class GymSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True)
    class Meta:
        model = Gym
        fields = ("id", "name", "location", "zip_code", "programs")