from django.db import models
from .center import Center

class Division(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # Add other relevant division fields here (e.g., description)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)  # Link to Center

    class Meta:
        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'

    def __str__(self):
        return self.name