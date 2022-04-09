from django.db import models

from django.template.defaultfilters import slugify

from PIL import Image
import random
import uuid
from io import BytesIO
from django.core.files import File
# import mptt
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone



def rand_slug():
    return str(uuid.uuid4()).replace('-','')




class Category(MPTTModel):

    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.SET_NULL,  null=True, blank=True, related_name='children'
    )

    tags = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='category/images')
    slug = models.SlugField(max_length=300,null=True, blank=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    popularity = models.BigIntegerField(default=0)

    class MPTTMeta:
        order_insertion_by = ['name']

    def compress_image(self, image, size=(1000, 1000)):
        img = Image.open(image)
        if img.mode in ("RGBA", "P"):
            img = img.convert('RGB')
        w, h = img.size
        if w > size[0] or h > size[1]:
            img.thumbnail(size)
        thumb_io = BytesIO()
        img_name = image.name
        splitted = img_name.rsplit('.', 1)  # split only in two parts
        im_format = 'webp'
        img.save(thumb_io, im_format)
        thumbnail = File(thumb_io, name=splitted[0]+'.webp')
        return thumbnail
    
  

    def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)
        if not self.slug:
            self.slug = slugify(self.name)
            self.tags=self.name.lower()
        super(Category, self).save(*args, **kwargs)

        
        
    
    def get_absolute_url(self):
        return self.slug


    def __str__(self):
        return self.name