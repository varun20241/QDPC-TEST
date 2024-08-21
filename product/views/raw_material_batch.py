from qdpc.core.modelviewset import BaseModelViewSet
from rest_framework import status
from qdpc.core import constants
from django.shortcuts import render, redirect
from qdpc_core_models.models.raw_materialbach import RawMaterialBatch
from qdpc_core_models.models.raw_material import RawMaterial
from qdpc_core_models.models.unit import Unit
from product.serializers.rawmaterial_batch_serializer import RawMaterialBatchSerializer
from product.services.raw_material_service import RawmaterialService




class RawMatrialBatchFetchView(BaseModelViewSet):
  

    def get(self,request,pk=None):
        if pk:
            data={}
            is_success = False
            message = constants.USER_FETCH_FAILED
            status_code = status.HTTP_403_FORBIDDEN
            try:
                is_success, status_code, data, message = RawmaterialService.get_rawmateril_batch_list(pk=None)
                context = {'batches':data}
                return render(request,'batchlist.html',context)

            except Exception as ex:
                success = False
                message = constants.USER_FETCH_FAILED
                status_code = status.HTTP_400_BAD_REQUEST
                
                return self.render_response(data,success, message, status_code)
        else:
            raw_material_batches =self.get_all_obj(model_name=RawMaterialBatch)
            serializer = RawMaterialBatchSerializer(raw_material_batches, many=True)
            context = {'batches': serializer.data}

           
        return render(request,'batchlist.html',context)
    
   
   

class RawMatrialBatchAddView(BaseModelViewSet):

    def get(self,request):
        raw_materials =self.get_all_obj(model_name=RawMaterial)
        units = self.get_all_obj(model_name=Unit)
        raw_materials_with_expiry = []
        for raw_material in raw_materials:
            expiry_date = raw_material.expiry_date
            raw_materials_with_expiry.append({
                'id': raw_material.id,
                'name': raw_material.name,
                'grade': raw_material.grade,
                'shelf_life_value': raw_material.shelf_life_value,
                'shelf_life_unit': raw_material.shelf_life_unit,
                'expiry_date': expiry_date
            })
        context = {
            'raw_materials': raw_materials_with_expiry,
            'units': units,
        }

        return render(request,'batch.html',context)
    
    def post(self, request):
        success=False
        message=constants.USERNAME_PASSWORD_EMPTY
        status_code=status.HTTP_403_FORBIDDEN
        data=request.data
      
        try:
            if data:
                success, status_code, data, message = RawmaterialService.add_rawmaterial_bach_add(data=data)
           
        except Exception as ex:
            success = False
            message = constants.USERNAME_PASSWORD_EMPTY
            status_code = status.HTTP_400_BAD_REQUEST
            
        return self.render_response(data, success, message, status_code)







    
