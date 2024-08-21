from rest_framework import serializers
from qdpc_core_models.models.raw_materialbach import RawMaterialBatch
from product.serializers.rawmateriallist_serializer import RawMaterialSerializer
from product.serializers.unit_serializer import UnitSerializer
from qdpc_core_models.models.raw_material import RawMaterial
from qdpc_core_models.models.unit import Unit


class RawMaterialBatchSerializer(serializers.ModelSerializer):
    raw_material = serializers.PrimaryKeyRelatedField(queryset=RawMaterial.objects.all())
    batch_size_unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    raw_material_name = serializers.SerializerMethodField()
    expiry_date = serializers.SerializerMethodField()

    class Meta:
        model = RawMaterialBatch
        fields = [
            'id', 
            'raw_material', 
            'raw_material_name',
            'batch_id', 
            'procurement_date', 
            'expiry_date', 
            'batch_size_value', 
            'batch_size_unit', 
            'packing_details'
        ]

    def get_raw_material_name(self, obj):
        return obj.raw_material.name

    def get_expiry_date(self, obj):
        # Calculate the expiry date based on the raw material's shelf life
        return obj.raw_material.expiry_date

    def create(self, validated_data):
        raw_material = validated_data.pop('raw_material')
        batch_size_unit = validated_data.pop('batch_size_unit')

        raw_material_batch = RawMaterialBatch.objects.create(
            raw_material=raw_material,
            batch_size_unit=batch_size_unit,
            **validated_data
        )
        return raw_material_batch

    def update(self, instance, validated_data):
        raw_material = validated_data.pop('raw_material', None)
        batch_size_unit = validated_data.pop('batch_size_unit', None)

        if raw_material:
            instance.raw_material = raw_material
        if batch_size_unit:
            instance.batch_size_unit = batch_size_unit

        instance.batch_id = validated_data.get('batch_id', instance.batch_id)
        instance.procurement_date = validated_data.get('procurement_date', instance.procurement_date)
        instance.batch_size_value = validated_data.get('batch_size_value', instance.batch_size_value)
        instance.packing_details = validated_data.get('packing_details', instance.packing_details)

        # Recalculate expiry date based on the updated data
        instance.expiry_date = instance.raw_material.expiry_date

        instance.save()
        return instance
