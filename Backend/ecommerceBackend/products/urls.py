from django.urls import path
# from mainApp import views
from .views import *

urlpatterns = [
    # path("", Index),
    path("add-product", AddProduct.as_view()),
    path("update-product", UpdateProduct.as_view()),
    path("add-to-cart", AddToCart.as_view()),
    path("add-to-wishlist", AddToWishlist.as_view()),
    path("remove-from-cart", RemovedFromCart.as_view()),
]
