from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.authentication.models import User
from .forms import UserCreationForm, UserChangeForm

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', "balance"]

    form = UserChangeForm
    add_form = UserCreationForm

    add_fieldsets = ((None, {"fields": ("email", "password1", "password2")}),)
    fieldsets = (
        (None, {"fields": ("email", "password", "balance")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )

    ordering = ['-id']