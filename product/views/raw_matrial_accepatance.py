from rest_framework import status
from qdpc.core import constants
from rest_framework.response import Response
# from qdpc.services.rawmaterial_service import RawMaterialService
from qdpc.core.modelviewset import BaseModelViewSet
from django.shortcuts import render, redirect
from qdpc_core_models.models.raw_materialbach import RawMaterialBatch
from qdpc_core_models.models.unit import Unit
from qdpc_core_models.models.raw_material import RawMaterial
from qdpc_core_models.models.acceptance_test import AcceptanceTest
from product.serializers.acceptence_test_serializer import AcceptanceTestSerializer

class RawMaterialAcceptanceTestAdd(BaseModelViewSet):
    """ Raw Material List API for qdpc application"""
 
    def get(self, request):
        raw_material_batch = self.get_all_obj(model_name=RawMaterial)
        units = self.get_all_obj(model_name=Unit)
        context = {
            'raw_materials': raw_material_batch,
            'units':units
        }
        return render(request, 'rmacceptance-test.html',context)
    
    def post(self, request):
        print(request.data)
        # Validate the incoming data using the serializer
        serializer = AcceptanceTestSerializer(data=request.data)

        if serializer.is_valid():
            print("it is valid")
            # If the data is valid, save the serializer
            serializer.save()
            success = True
            message ='Acceptance test added successfully!'
            data= serializer.data
            status_code = status.HTTP_201_CREATED
            
        else:
            print("it is not valid")
            print(serializer.errors)
            success = False
            message ='Validation failed.'
            status_code = status.HTTP_400_BAD_REQUEST
            data={}
            
        return self.render_response(data, success, message, status_code)







class RawMaterialAcceptanceTestList(BaseModelViewSet):
    """ Raw Material Acceptance Test List API """

    def get(self, request):
        acceptance_tests = AcceptanceTest.objects.all()

        # Serialize the data
        test_serializer = AcceptanceTestSerializer(acceptance_tests, many=True)

        # return Response(test_serializer.data)
        

        context = {
            'acceptance_tests': test_serializer.data,
        }
        return render(request, 'rmtest-list.html', context)
    












    