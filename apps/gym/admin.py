from django.contrib import admin

from apps.gym.models import Gym
# Register your models here.

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "zip_code"]

    search_fields = ["name", "location",]
