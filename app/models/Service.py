from django.db import models
from app.models import TempData
from app.models.Shelter import Shelter


class Service(models.Model):
    shelter = models.ForeignKey(Shelter, max_length=50, on_delete=models.PROTECT)
    status = models.CharField(max_length=50, choices=TempData.ServiceStatus)
    volunteer = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TempData.ServiceType)
    required_ad = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=40, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Service:" % (
        )
