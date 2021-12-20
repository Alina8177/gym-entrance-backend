from django.db import models

import uuid

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    location = models.CharField(max_length=100, null=True, blank=False)
    zip_code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField()
    gym = models.ForeignKey("gym.Gym", null=True, blank=True, on_delete=models.CASCADE, related_name='programs')
    is_archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class OrderStatus(models.TextChoices):
    OPEN = ("open", "Open")
    PAID = ("paid", "Paid")
    ACTIVE = ("active", "Active")
    INACTIVE = ("inactive", "Inactive")

class Order(models.Model):
    uid = models.UUIDField(default=uuid.uuid4)
    order_by = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(default=OrderStatus.OPEN, choices=OrderStatus.choices, max_length=10)
    programs = models.ManyToManyField('gym.Program')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.uid)
