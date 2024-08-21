from rest_framework import serializers
from qdpc_core_models.models.acceptance_test import AcceptanceTest

class AcceptanceTestSerializer(serializers.ModelSerializer):
    raw_material_name = serializers.SerializerMethodField()

    class Meta:
        model = AcceptanceTest
        fields = ['id', 'raw_material','value','raw_material_name','name', 'specification', 'sampling_plan', 'reevaluation_frequency_value', 'reevaluation_frequency_unit', 'reevaluation_frequency']  

    
    def get_raw_material_name(self, obj):
        return obj.raw_material.name if obj.raw_material else None
    

    def validate_reevaluation_frequency_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("Reevaluation frequency value must be greater than 0.")
        return value