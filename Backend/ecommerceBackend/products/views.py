from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerceBackend.customPermissions import IsSuperUser
import datetime
import json
from bson import ObjectId
from ecommerceBackend.customauthentication import JWTAuthentication
from ecommerceBackend.utils import BasicUtils

BasicUtils = BasicUtils()

# Create your views here.
Products = settings.DB['products']
Wishlist = settings.DB['wishlist']
RemovedWishlist = settings.DB['removed-wishlist']
Cart = settings.DB['cart']
RemovedCart = settings.DB['removed-cart']


class AddProduct(APIView):
    permission_classes = (IsSuperUser, )

    def post(self, request):
        current_time = datetime.datetime.now()
        finalData = {}
        data = request.data

        for d in data:
            try:
                # print("try: ")
                # print(type(data[d]))
                finalData.update({d: json.loads(data[d])})
            except:
                # print("except")
                finalData.update({d: data[d]})

        finalData.update({"clicked": 0})
        finalData.update({"wishlist_count": 0})
        finalData.update({"cart_count": 0})
        finalData.update({"created_at": current_time})
        finalData.update({"updated_at": current_time})

        Products.insert_one(finalData)

        result = {
            "status": True,
            "message": "Product Added",
            "status_code": 201
        }
        return Response(result, status=status.HTTP_201_CREATED)


class UpdateProduct(APIView):
    permission_classes = (IsSuperUser, )

    def post(self, request):

        current_time = datetime.datetime.now()
        finalData = {}
        data = request.data
        print(data)
        old_product = Products.find_one({"_id": ObjectId(data.get("_id"))})
        print(old_product)
        if not old_product:
            result = {
                "status": False,
                "message": "Product does'nt exists",
                "status_code": 404
            }
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        for d in data:
            try:
                finalData.update({d: json.loads(data[d])})
            except:
                print(data[d])

        finalData.update({"clicked": 0})
        finalData.update({"wishlist_count": 0})
        finalData.update({"cart_count": 0})
        finalData.update({"created_at": current_time})
        finalData.update({"updated_at": current_time})
        print(finalData)
        Products.update_one({'_id': ObjectId(data.get("_id"))}, {
                            '$set': finalData})
        result = {
            "status": True,
            "message": "Product updated",
            "status_code": 200
        }
        return Response(result, status=status.HTTP_200_OK)



class AddToWishlist(APIView):
    authentication_classes = (JWTAuthentication, )
    def post(self, request):
        payload = request.data
        user_id, user_role = BasicUtils.get_user_from_request(request)
        try:
            product_id = payload.get('product_id')
            if not product_id:
                return Response(
                    {
                        'status': False,
                        "message": 'Product id not provided!',
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)

            product = Products.find_one({'_id': ObjectId(product_id)}, {'_id': 1})

            if not product:
                return Response(
                    {
                        'status': False,
                        "message": "Product doesn't exists!",
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)

            exist_wishlist = Wishlist.find_one({
                    'user_id': ObjectId(user_id),
                    'product_id': ObjectId(product_id)}, {"_id": 0})
            
            if exist_wishlist:
                Wishlist.delete_one(
                {
                    'user_id': ObjectId(user_id),
                    'product_id': ObjectId(product_id)
                })

                exist_wishlist['removed_at'] = datetime.datetime.now()

                removed_wishlist_product = RemovedWishlist.find_one({"user_id": ObjectId(user_id), "product_id": ObjectId(product_id)})

                if removed_wishlist_product:
                    RemovedWishlist.update_one({"user_id": ObjectId(user_id), "product_id": ObjectId(product_id)}, {"$set": exist_wishlist})
                else:
                    RemovedWishlist.insert_one(exist_wishlist)

                Products.update_one({'_id': ObjectId(product_id)}, {"$inc": {"wishlist_count": -1}})
                return Response(
                    {
                        'status': False,
                        "message": "Removed from wishlist!",
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                Wishlist.insert_one(
                    {
                        'user_id': ObjectId(user_id),
                        'product_id': ObjectId(product_id),
                        'created_at': datetime.datetime.now()
                    }
                )
                Products.update_one({'_id': ObjectId(product_id)}, {"$inc": {"wishlist_count": 1}})
                return Response({
                    'status': True,
                    "message": 'Added to wishlist',
                    'status_code': 200
                }, status=status.HTTP_200_OK)

        except Exception as e:

            return Response({
                'status': False,
                "message": 'Invalid product id',
                'status_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class AddToCart(APIView):
    authentication_classes = (JWTAuthentication, )
    def post(self, request):
        payload = request.data
        user_id, user_role = BasicUtils.get_user_from_request(request)
        try:
            product_id = payload.get('product_id')
            if not product_id:
                return Response(
                    {
                        'status': False,
                        "message": 'Product id not provided!',
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)

            product = Products.find_one({'_id': ObjectId(product_id)}, {'_id': 1})

            if not product:
                return Response(
                    {
                        'status': False,
                        "message": "Product doesn't exists!",
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)

            exist_cart = Cart.find_one({
                    'user_id': ObjectId(user_id),
                    'product_id': ObjectId(product_id)})
            
            if exist_cart:
                return Response(
                    {
                        'status': False,
                        "message": "Product has already added to the cart!",
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                Cart.insert_one(
                    {
                        'user_id': ObjectId(user_id),
                        'product_id': ObjectId(product_id),
                        'created_at': datetime.datetime.now()
                    }
                )
                Products.update_one({'_id': ObjectId(product_id)}, {"$inc": {"cart_count": 1}})
                return Response({
                    'status': True,
                    "message": 'Added to Cart',
                    'status_code': 200
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': False,
                "message": 'Invalid product id',
                'status_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)



class RemovedFromCart(APIView):
    authentication_classes = (JWTAuthentication, )
    def post(self, request):
        payload = request.data
        user_id, user_role = BasicUtils.get_user_from_request(request)
        try:
            product_id = payload.get('product_id')
            if not product_id:
                return Response(
                    {
                        'status': False,
                        "message": 'Product id not provided!',
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)

            product = Products.find_one({'_id': ObjectId(product_id)}, {'_id': 1})

            if not product:
                return Response(
                    {
                        'status': False,
                        "message": "Product doesn't exists!",
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)

            cart_product = Cart.find_one({'user_id': ObjectId(user_id), 'product_id': ObjectId(product_id)}, {"_id": 0})

            if not cart_product:
                return Response(
                    {
                        'status': False,
                        "message": "Product is not in cart!",
                        'status_code': 400
                    }, status=status.HTTP_400_BAD_REQUEST)

            Cart.delete_one(
                {
                    'product_id': ObjectId(product_id)
                }
            )

            cart_product['removed_at'] = datetime.datetime.now()

            removed_cart_product = RemovedCart.find_one({"user_id": ObjectId(user_id), "product_id": ObjectId(product_id)})
            if removed_cart_product:
                RemovedCart.update_one({"user_id": ObjectId(user_id), "product_id": ObjectId(product_id)}, {"$set": cart_product})
            else:
                RemovedCart.insert_one(cart_product)

            Products.update_one({'_id': ObjectId(product_id)}, {"$inc": {"cart_count": -1}})
            return Response({
                'status': True,
                "message": 'Removed from Cart',
                'status_code': 200
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': False,
                "message": 'Invalid product id',
                'status_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

