from django.urls import path
# from mainApp import views
from .views import *

urlpatterns = [
    # path("", Index),
    path("register", CreateRawUser.as_view()),
    path("auth/social", CreateSocialUser.as_view()),
    path("login", Login.as_view()),
    path("validate-token", ValidateToken.as_view())
]