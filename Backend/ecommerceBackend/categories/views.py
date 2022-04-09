from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.views import APIView

# from rest_framework.permissions import AllowAny
from ecommerceBackend.customauthentication import JWTAuthentication
from ecommerceBackend.customauthentication import AllowAll

from .models import *


def serializable_object(node):
    """Recurse into category tree to build a serializable object"""

    obj = {
        "id": node.id,
        "title": node.name,
        "slug": node.slug,
        "open": False,
        "image": node.image.url,  # DOMAIN came from models variable
        "level": node.level,
        
    }
    if len(node.get_children()):
        obj["subnav"] = [serializable_object(ch) for ch in node.get_children()]
    return obj

class GetCategories(APIView):
    authentication_classes = (AllowAll,)
    # authentication_classes = (JWTAuthentication, )
    def get(self, request):
        objects = []
        data=[]
        
        c = Category.objects.filter(level=0)
        for i in c:
            obj = serializable_object(i)
            objects.append(obj)

            # print(type(obj))
        # print(obj)
        sorted_popularity = Category.objects.order_by('-popularity')[:8]
        sorted_popularity = [{"title": node.name,
                "slug": node.slug,
                "image": node.image.url} for node in sorted_popularity]

        data.append(objects)
        data.append(sorted_popularity)
        # print(sorted_popularity)
        return Response(data)

