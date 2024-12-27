
from django.contrib import admin
from django.urls import path

from shop.views import index, products,product, contacts, formRequest, requests

app_name = 'shop'
urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('formRequest/', formRequest, name='formRequest'),
    path('requests/', requests, name='requests'),
    path('products/', products, name='products'),
    path('product/<int:product_id>/', product, name='product'),
]
