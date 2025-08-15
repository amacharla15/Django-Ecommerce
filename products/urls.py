from django.urls import path, include
from products import views

urlpatterns = [
    path('hello/',views.hello)
]
