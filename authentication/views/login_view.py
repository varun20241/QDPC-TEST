from rest_framework.views import APIView
from qdpc.core.modelviewset import BaseModelViewSet
from rest_framework import status
from rest_framework.response import Response
from qdpc.core import constants
class TestView(BaseModelViewSet):

    def get(self,request):
        status_code = 200
        is_success = True
        message = constants.LOGIN_SUCCESS
        data = {"user:Rohini"}

        return self.render_response(data, is_success, message,
                                    status_code)
