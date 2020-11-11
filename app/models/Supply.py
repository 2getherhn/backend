from django.db import models
from app.models import TempData


class Supply(models.Model):
    name = models.CharField(max_length=150)
    enabled = models.BooleanField(default=True)
    required_by = models.CharField(max_length=50, choices=TempData.RequiredBy)
    priority = models.CharField(max_length=50, choices=TempData.Priorities)

    created_by = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=40, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Supply: " % (
        )
