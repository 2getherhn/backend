from django.db import models
from app.models import TempData
from app.models.Shelter import Shelter


class Requisition(models.Model):
    shelter = models.ForeignKey(Shelter, max_length=50, on_delete=models.PROTECT)
    shipping = models.BooleanField(default=False)
    all_terrain_vehicle = models.BooleanField(default=False)
    required_ad = models.DateTimeField(auto_now_add=True)
    fulfilled_at = models.DateTimeField(auto_now_add=False)

    created_by = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=40, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Requisition:" % (
        )
