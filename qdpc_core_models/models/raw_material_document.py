from django.db import models
from qdpc_core_models.models.raw_material import RawMaterial
from qdpc_core_models.models.document_categary import DocumentCategory


class RawMaterialDocument(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE)
    issue_no = models.CharField(max_length=255)
    revision_no = models.CharField(max_length=255)
    release_date = models.DateField()
    approved_by = models.CharField(max_length=255)
    document = models.FileField(upload_to='Rrawmaterial/Documents/')
    validity = models.IntegerField(help_text="Validity in years")

    def __str__(self):
        return f"{self.title} - {self.raw_material.name}"