from django.db import models

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    location = models.CharField(max_length=100, null=True, blank=False)
    zip_code = models.CharField(max_length=50, null=True, blank=True)