from django.db import models
from app.models import TempData
from app.models.Shelter import Shelter


class ShippingRequest(models.Model):
    shelter = models.ForeignKey(Shelter, max_length=50, on_delete=models.PROTECT)
    destination = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=TempData.ShippintStatus)
    scheduled_at = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=40, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ShippingRequest:" % (
        )
