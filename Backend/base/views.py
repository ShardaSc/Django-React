from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.products import Prodcuts  
from rest_framework import status

@api_view(['GET'])
def all_products(request):
    return Response(Prodcuts)

@api_view(['GET'])
def get_product(request,ID):
    if request.method == 'GET':
        for product in Prodcuts:
            if product['_id'] ==str(ID):
                return Response(product)
        return Response(status.HTTP_404_NOT_FOUND)