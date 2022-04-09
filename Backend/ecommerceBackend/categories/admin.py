from django.contrib import admin

from .models import *
from mptt.admin import DraggableMPTTAdmin

admin.site.register(Category, DraggableMPTTAdmin)