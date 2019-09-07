from django.shortcuts import render
from rest_framework.views import APIView

class AdminLoginAPIView(APIView):

    # Request URL:http://127.0.0.1:8000/meiduo_admin/authorizations/
    # Request Method:OPTIONS
    def post(self, request):

        # Access-Control-Allow-Origin:*
        pass
