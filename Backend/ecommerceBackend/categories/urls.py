from django.urls import path
# from mainApp import views
from .views import *

urlpatterns = [
    # path("", Index),
    path("categories", GetCategories.as_view()),
]