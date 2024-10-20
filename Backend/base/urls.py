from django.urls import path
from base import views

urlpatterns = [
        path('allproducts',views.all_products),
        path('products/<int:ID>',views.get_product)
]