from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.db.models import Q
from mainApp.models import *
from django.core.files import File
from django.conf import settings
from decimal import *
# from .models import *
import datetime
from PIL import Image
from io import BytesIO
import json
import itertools
import glob
import uuid
from rest_framework.permissions import IsAuthenticated
from intriosBackend.CustomPermissions import IsSuperUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.files.storage import default_storage

# Database and collections

DB = settings.DB
Products = DB['products']
SiteSettings = DB['site-settings']

current_time = datetime.datetime.now()
current_time = current_time.strftime("%d/%m/%Y %H:%M:%S")


def compress_image(image, size=(1000, 1000), format="webp"):
    img = Image.open(image)
    if img.mode in ("RGBA", "P"):
        img = img.convert('RGB')
    w, h = img.size
    if w > size[0] or h > size[1]:
        img.thumbnail(size)
    thumb_io = BytesIO()
    img_name = image.name
    splitted = img_name.rsplit('.', 1)  # split only in two parts
    # im_format = 'JPEG'
    # img.save(thumb_io, im_format, quality=70)
    # thumbnail = File(thumb_io, name=splitted[0]+'.jpg')
    im_format = format
    img.save(thumb_io, im_format)
    thumbnail = File(thumb_io, name=splitted[0]+'.'+format)
    return thumbnail



class UploadMedia(APIView):
    # permission_classes = (IsSuperUser, )
    def post(self, request):
        # print(request.data)
        data = request.data

        for i in data:
            img = compress_image(data[i])
            f_name = settings.MEDIA_URL+"/products/images/"+img.name
            # f_name = img.name
            file_name = default_storage.save(f_name, img)
            # default_storage.delete("Screenshot from 2021-09-02 23-37-56.webp")
            # print(default_storage.listdir("/"))
            # default_storage.url("Screenshot from 2021-09-28 21-24-19.webp")

        # print(database.Products.find_one({"name": "sourav", "score": 2}))
        return Response(status = status.HTTP_201_CREATED) 