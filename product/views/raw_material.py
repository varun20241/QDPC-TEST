from qdpc.core.modelviewset import BaseModelViewSet
from rest_framework import status
from qdpc.core import constants
from django.shortcuts import render, redirect
from qdpc_core_models.models.raw_material import RawMaterial
from product.serializers.rawmateriallist_serializer import RawMaterialSerializer
from product.services.raw_material_service import RawmaterialService
from qdpc_core_models.models.supplier import Suppliers
from qdpc_core_models.models.source import Sources
from qdpc_core_models.models.supplier import Suppliers
from qdpc_core_models.models.source import Sources
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  



class RawMatrialListFetchView(BaseModelViewSet):
  

    def get(self,request,batch_id=None):

        if batch_id:
            raw_material_data = self.get_raw_material_data(batch_id)
            all_suppliers = self.get_all_obj(model_name=Suppliers)
            all_sources = self.get_all_obj(model_name=Sources)
            raw_material_data['all_suppliers'] = [{'id': suppliers.id, 'name': suppliers.name} for suppliers in all_suppliers]
            raw_material_data['all_sources'] = [{'id': sources.id, 'name': sources.name} for sources in all_sources]
            return Response({'data': raw_material_data}, status=status.HTTP_200_OK)
        else:
            raw_material_list =self.get_all_obj(model_name=RawMaterial)
            serializer = RawMaterialSerializer(raw_material_list, many=True)
            context = {'batches': serializer.data}
           
            return render(request,'material.html',context)
    

    def get_raw_material_data(self, batch_id):
        raw_material = get_object_or_404(RawMaterial, id=batch_id)
        raw_material_data = {
            'id': raw_material.id,
            'name': raw_material.name,
            'sources': [source.id for source in raw_material.sources.all()],
            'suppliers': [supplier.id for supplier in raw_material.suppliers.all()],
            'grade': raw_material.grade,
            'shelf_life_value': raw_material.shelf_life_value,
            'shelf_life_unit': raw_material.shelf_life_unit,
            'user_defined_date': raw_material.user_defined_date,
            'expiry_date': raw_material.expiry_date,
        }
        
        

        return raw_material_data
    
    def put(self, request, batch_id):
        try:
            raw_material = RawMaterial.objects.get(id=batch_id)
        except RawMaterial.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        print(request.data)
        serializer = RawMaterialSerializer(raw_material, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











class RawMaterialAdd(BaseModelViewSet):
    """ Raw Material List API for qdpc application"""
 
    def get(self, request):
        sources =self.get_all_obj(model_name=Sources)
        suppliers = self.get_all_obj(model_name=Suppliers)
        context = {
            'sources': sources,
            'suppliers': suppliers,
        }
        return render(request, 'addmaterial.html',context)
    
    def post(self, request):
        data=request.data
        success=False
        message=constants.USERNAME_PASSWORD_EMPTY
        status_code=status.HTTP_403_FORBIDDEN

        try:
            if data:
                success, status_code, data, message = RawmaterialService.add_rawmaterial_add(data=data)
                print( success, status_code, data, message,"what i got afer testing")

        except Exception as ex:
            data={}
            success = False
            message = constants.USERNAME_PASSWORD_EMPTY
            status_code = status.HTTP_400_BAD_REQUEST
            
        return self.render_response(data, success, message, status_code)




    


    