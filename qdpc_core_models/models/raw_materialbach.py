
from django.db import models
from django.utils import timezone
from datetime import timedelta
from qdpc_core_models.models.raw_material import RawMaterial
from qdpc_core_models.models.unit import Unit


class RawMaterialBatch(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, related_name='batches')
    batch_id = models.CharField(max_length=100, unique=True)
    procurement_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    batch_size_value = models.FloatField()
    batch_size_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='batch_sizes')
    packing_details = models.TextField()

    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = self.raw_material.calculate_expiry_date(self.procurement_date)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.raw_material.name} - Batch {self.batch_id}"
