from django.contrib import admin

from apps.gym.models import Gym, Program, Order

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "zip_code"]

    search_fields = ["name", "location",]

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "gym", "is_archive"]

    search_fields = ["name",]

    list_filter = ["is_archive",]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["uid", "order_by", "status", "total"]

    list_filter = ["status"]

