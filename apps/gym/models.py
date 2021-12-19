from django.db import models

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    location = models.CharField(max_length=100, null=True, blank=False)
    zip_code = models.CharField(max_length=50, null=True, blank=True)


class Program(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField()
    gym = models.ForeignKey("gym.Gym", null=True, blank=True, on_delete=models.CASCADE, related_name='programs')
    is_archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)