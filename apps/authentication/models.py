from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.fields import DecimalField


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not all([email, password]):
            raise ValueError("Users must have an email address and password!")

        email = self.normalize_email(email)
        user = self.model(email=email)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email of user", null=False, blank=False, max_length=40, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()
    
    def __str__(self) -> str:
        return self.email


class PaymentStatus(models.TextChoices):
    PAID = ("paid", "Paid")
    CANCELED = ("canceled", "Canceled")

class Payment(models.Model):
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE, null=True, related_name='payments')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default=PaymentStatus.PAID, choices=PaymentStatus.choices)


class ChargeStatus(models.TextChoices):
    SUCCESS = ("success", "Success")
    CANCELED = ("canceled", "Canceled")


class Charge(models.Model):
    order = models.ForeignKey('gym.Order', on_delete=models.CASCADE, related_name='charges')
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='charges')
    status = models.CharField(max_length=10, choices=ChargeStatus.choices, default=ChargeStatus.SUCCESS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)