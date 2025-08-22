from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.

def hello(request):
    data=Products.objects.all()
    d=data[0]
    d.name="lkj"
    d.save()
    data=Products.objects.all()
    print(data[0].name)
    return HttpResponse("Hello World")
#decorator
@api_view(['GET','POST'])
def get_Products(request):
    data=Products.objects.all()
    serializedProducts=ProductSerializer(data, many=True)
    return Response(serializedProducts.data)
@api_view(['GET'])
def get_Product(request, pk):
    data=Products.objects.get(pk=pk)
    serializedProducts=ProductSerializer(data)
    return Response(serializedProducts.data)

