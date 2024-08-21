from rest_framework import serializers
from qdpc_core_models.models.raw_material import RawMaterial
from product.serializers.source_serializer import SourcesSerializer
from product.serializers.supplier_serializer import SuppliersSerializer
from qdpc_core_models.models.source import Sources
from qdpc_core_models.models.supplier import Suppliers


class RawMaterialSerializer(serializers.ModelSerializer):
    sources = serializers.PrimaryKeyRelatedField(queryset=Sources.objects.all(), many=True)
    suppliers = serializers.PrimaryKeyRelatedField(queryset=Suppliers.objects.all(), many=True)
    sources = serializers.PrimaryKeyRelatedField(queryset=Sources.objects.all(), many=True)
    suppliers = serializers.PrimaryKeyRelatedField(queryset=Suppliers.objects.all(), many=True)
    expiry_date = serializers.SerializerMethodField()
    source_names = serializers.SerializerMethodField()
    supplier_names = serializers.SerializerMethodField()

    

    class Meta:
        model = RawMaterial
        fields = [
            'id',
            'name',
            'sources',
            'suppliers',
            'grade',
            'shelf_life_value',
            'shelf_life_unit',
            'user_defined_date',
            'source_names',
            'supplier_names',
            
            'expiry_date',
        ]

    def validate_shelf_life_value(self, value):
        """Ensure shelf_life_value is numeric (float or integer)."""
        if not isinstance(value, (float, int)):
            raise serializers.ValidationError("Shelf life value must be a numeric type.")
        return value
    def get_expiry_date(self, obj):
        return obj.expiry_date
    def get_source_names(self, obj):
        return [source.name for source in obj.sources.all()]

    def get_supplier_names(self, obj):
        return [supplier.name for supplier in obj.suppliers.all()]


    def create(self, validated_data):
        sources = validated_data.pop('sources', [])
        suppliers = validated_data.pop('suppliers', [])

        raw_material = RawMaterial.objects.create(**validated_data)

        raw_material.sources.set(sources)
        raw_material.suppliers.set(suppliers)

        return raw_material

    def update(self, instance, validated_data):
        sources = validated_data.pop('sources', None)
        suppliers = validated_data.pop('suppliers', None)

        instance.name = validated_data.get('name', instance.name)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.shelf_life_value = validated_data.get('shelf_life_value', instance.shelf_life_value)
        instance.shelf_life_unit = validated_data.get('shelf_life_unit', instance.shelf_life_unit)
        instance.user_defined_date = validated_data.get('user_defined_date', instance.user_defined_date)
        instance.save()

        if sources is not None:
            instance.sources.set(sources)

        if suppliers is not None:
            instance.suppliers.set(suppliers)

        return instance
