from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django import Jsonresponse
# Create your views here.

def hello(request):
    data=Products.objects.all()
    d=data[0]
    d.name="lkj"
    d.save()
    data=Products.objects.all()
    print(data[0].name)
    return HttpResponse("Hello World")
def allProducts(request):
    return JsonRe
