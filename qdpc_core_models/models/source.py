from django.db import models


class Sources(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)


     class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'

     def __str__(self):
        return self.name
     
     