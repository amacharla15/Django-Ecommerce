from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.

def hello(request):
    data=Products.objects.all().order_by('id')
    
    print(data)
    if(data.exists()):
        data.name="abc"
        data.save()
    return HttpResponse("Hello World")
