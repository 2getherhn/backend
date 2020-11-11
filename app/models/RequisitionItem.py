from django.db import models
from app.models.Requisition import Requisition
from app.models.Supply import Supply


class RequisitionItem(models.Model):
    requisition = models.ForeignKey(Requisition, max_length=50, on_delete=models.PROTECT)
    supply = models.ForeignKey(Supply, max_length=50, on_delete=models.PROTECT)
    desired_qty = models.IntegerField()
    provided_qty = models.IntegerField()

    created_by = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=40, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Requisition:" % (
        )
