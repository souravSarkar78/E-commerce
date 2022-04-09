from __future__ import annotations
from django.conf import settings
import hashlib



import re
from urllib.parse import urlsplit

import jwt
import tldextract
from django.conf import settings

class Validation(object):
    def generate_password(self, message):
        salt = settings.SECRET_KEY.encode()
        # salt = key.encode() # encode key
        dk = hashlib.pbkdf2_hmac('sha256', message.encode(), salt, 50000) # generate hash
        return dk.hex() # erturn hexed hash

    
    def match_paassword(self, password_true, password_given):
        # print(self.generate_password(password_given))
        # if password_true == self.generate_password(password_given):
        if password_true == self.generate_password(password_given):
            return True
        else:
            return False




class BasicUtils:

    def get_base_domain(self, url):
        """Takes raw url or Email ID and returns the Base Domain"""
        split_url = urlsplit(url).netloc
        if not split_url:
            url = '//' + url
            split_url = urlsplit(url).netloc
        if '@' in split_url:
            elements = re.split(r'[@]', split_url)
            split_url = elements[1]

        extract_result = tldextract.extract(split_url)
        base_domain = extract_result.domain+'.'+extract_result.suffix
        return base_domain

    def get_user_from_request(self, request):

        authorization_token = request.headers.get('Authorization')
        payload = jwt.decode(
            authorization_token,
            settings.SECRET_KEY, algorithms=['HS256'],
        )

        user_id = payload.get('user_id')
        user_role = payload.get('role')

        return user_id, user_role