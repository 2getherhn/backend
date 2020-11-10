from django.db import models
from app.models import TempData


class Shelter(models.Model):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TempData.ShelterTypes)

    created_by = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=40, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Shelter: %s Name: %s, Type: %s" % (
            self.number,
            self.name,
            self.type
        )
