from __future__ import annotations

from rsa import verify

# import logging
# import os

import jwt
from bson import ObjectId
from django.conf import settings
# from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
# from rest_frameword.permissions import BasePermission

# Database (Users collection)
users = settings.DB['users']


# class CSRFCheck(CsrfViewMiddleware):
#     def _reject(self, request, reason):
#         return reason

# Custom authentication class


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        print("Yoo")
        authorization_token = request.headers.get('Authorization')
        print(authorization_token)
        if authorization_token is None:
            raise exceptions.AuthenticationFailed('Access Token Required')
        try:
            header_data = jwt.get_unverified_header(authorization_token)
            payload = jwt.decode(
                authorization_token,                        
                settings.SECRET_KEY, 
                algorithms=[header_data['alg'], ]
            )
            # print(payload)
            # print(datetime.now())
            user_id = payload.get('user_id')
            # user_role = payload.get('role') # currently not in use
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Access Token expired')
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid Token')

        user = users.find_one({'_id': ObjectId(user_id)})
        if not user:
            raise exceptions.AuthenticationFailed('User not found')
        return (1, None)

    # def enforce_csrf(self, request):
    #     check = CSRFCheck()
    #     check.process_request(request)
    #     reason = check.process_view(request, None, (), {})
    #     if reason:
    #         raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        authorization_token = request.headers.get('x-api-key')
        if authorization_token is None:
            raise exceptions.AuthenticationFailed('Token Key Missing!')
        if authorization_token == settings.X_API_KEY:
            return (1, None)
        else:
            raise exceptions.AuthenticationFailed('Token Mismatch!')


class AllowAll(BaseAuthentication):
    def authenticate(self, request):
        print("Allow All")
        return (1, None)
