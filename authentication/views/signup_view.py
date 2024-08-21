from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from authentication.serializers.signup_serializer import UserSignupSerializer
from qdpc.core.modelviewset import  BaseModelViewSet
from qdpc.core import constants
from qdpc.services.login_service import LoginService
from qdpc_core_models.models.center import Center
from qdpc_core_models.models.division import Division
from qdpc_core_models.models.user_type import UserType

from django.shortcuts import render, redirect

class Signup(BaseModelViewSet):
    """ Signup API for qdpc application"""


    def get(self,request):
        "Handle request for loading the register template"
        context = {
            'divisions': self.get_all_obj(model_name=Division),
            'centers': self.get_all_obj(model_name=Center),
            'user_types': self.get_all_obj(model_name=UserType),
        }

        return render(request,'regn.html',context)
  

    def post(self, request):
        """ Handle POST requests to register a new user """
        # print("POST request received at Signup endpoint")  # Debug statement
        # print(f"Request data: {request.data}")  # Debug statement

        data = {}
        is_success = False
        message = constants.SIGNUP_FAILED
        status_code = status.HTTP_400_BAD_REQUEST

        print(request.data)
        try :
            data=request.data
            if data:
                is_success, status_code, data, message = LoginService.signup_user(data=data)
        except Exception as ex:
            success = False
            message = constants.SIGNUP_FAILED
            status_code = status.HTTP_400_BAD_REQUEST
            
        return self.render_response(data, is_success, message, status_code)