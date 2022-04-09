# Create your views here.
from turtle import delay
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerceBackend.utils import Validation
from ecommerceBackend.customauthentication import JWTAuthentication
from .auth import *

from django.conf import settings
# Collections
Users = settings.DB['users']

Validation = Validation()


class CreateRawUser(APIView):
    # permission_classes = (AllowAny,)
    def post(self, request):
        try:
            payload = request.data.dict()
            
            result = create_raw_user(**payload)

            if result.get("status"):
                return Response(result)
            else:
                return Response(result, status=status.HTTP_403_FORBIDDEN)

        except:
            return Response({"status": False,
                            "message": "User can't be created!"},
                            status=status.HTTP_403_FORBIDDEN)


class CreateSocialUser(APIView):
    # permission_classes = (AllowAny,)
    def post(self, request):
        try:
            token = request.data.get('token')
            print(token)

            if token:
                result = athenticate_social_user(token)
                print(result)
                return Response(result)

            else:
                return Response({"status": False, "message": "Token Required"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": False,
                            "message": "User can't be created!",
                            "err_msg": str(e)},
                            
                            status=status.HTTP_403_FORBIDDEN)


class Login(APIView):
    # authentication_classes = (JWTAuthentication, )
    
    def post(self, request):
        payload = request.data
        print(payload)
        username = payload.get('username')
        password = payload.get('password')
        
        result = authenticate_user(username, password)
        if result.get('status_code')==200:
            return Response(result, status=status.HTTP_200_OK)
        if result.get('status_code')==401:
            return Response(result, status=status.HTTP_401_UNAUTHORIZED)
        if result.get('status_code')==404:
            return Response(result, status=status.HTTP_404_NOT_FOUND)


class ValidateToken(APIView):
    authentication_classes = (JWTAuthentication, )

    def post(self, request):
        return Response(True)