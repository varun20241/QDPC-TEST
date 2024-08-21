from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.abbreviation
