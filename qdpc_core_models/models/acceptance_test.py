from django.db import models
from .unit import Unit
from datetime import timedelta
from qdpc_core_models.models.raw_material import RawMaterial

class AcceptanceTest(models.Model):
    TIME_UNIT_CHOICES = [
        ('months', 'Months'),
        ('years', 'Years'),
    ]

    id = models.AutoField(primary_key=True)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, related_name='test_results')
    name = models.CharField(max_length=255)
    specification = models.CharField(max_length=255, blank=True)
    value=models.CharField(max_length=255, blank=True)
    sampling_plan = models.FileField(upload_to='acceptance_test_results/')
    reevaluation_frequency_value = models.PositiveIntegerField(default=12)
    reevaluation_frequency_unit = models.CharField(max_length=10, choices=TIME_UNIT_CHOICES, default='months')

    def __str__(self):
        return self.name

    @property
    def reevaluation_frequency(self):
        if self.reevaluation_frequency_unit == 'years':
            return timedelta(days=self.reevaluation_frequency_value * 365)
        return timedelta(days=self.reevaluation_frequency_value * 30)

    @property
    def sampling_plan_filename(self):
        if self.sampling_plan:
            return self.sampling_plan.name.split('/')[-1]
        return 'No file'
