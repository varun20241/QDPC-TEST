from django.db import models
# from qdpc_core_models.models.user import User
from .source import Sources
from .supplier import Suppliers
from datetime import timedelta


class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    sources = models.ManyToManyField(Sources, related_name='raw_materials')
    suppliers = models.ManyToManyField(Suppliers, related_name='raw_materials')
    grade = models.CharField(max_length=50)
    shelf_life_value = models.FloatField()  # The numeric value for shelf life
    shelf_life_unit = models.CharField(max_length=10, choices=[('days', 'Days'), ('months', 'Months')])
    user_defined_date = models.DateField()

    @property
    def expiry_date(self):
        if self.shelf_life_unit == 'days':
            return self.user_defined_date + timedelta(days=self.shelf_life_value)
        else:
            return self.user_defined_date + timedelta(days=self.shelf_life_value * 30)

    def __str__(self):
        return self.name
