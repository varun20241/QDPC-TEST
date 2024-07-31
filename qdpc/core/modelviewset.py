
from rest_framework.views import APIView
from rest_framework.response import Response 
from .helpers import ResponseInfo

class BaseModelViewSet(APIView):

    def __init__(self, **kwargs):
        super(BaseModelViewSet, self).__init__(**kwargs)
        self.response = ResponseInfo().response

    def render_response(self, data, success, message, status,
                        token="", data_to_list=True, actual_exception=None):

        if isinstance(data, dict):
            data = [data] if data else []

        response = self.response
        response['isSuccess'] = success
        if actual_exception:
            message = str(message) + " - " + str(actual_exception)
        response['message'] = message
        response['result'] = data
        response['status'] = status
        return Response(response)
