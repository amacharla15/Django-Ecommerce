from django.urls import path, include
from products import views

urlpatterns = [
    path('hello/',views.hello),
    path('allProducts/', views.get_Products),
    path('Product/<int:pk>', views.get_Product),
]
