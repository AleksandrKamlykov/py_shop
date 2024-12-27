
from django.contrib import admin
from django.urls import path, include
from api.models import CtegoryResource, ProductResource
from tastypie.api import Api

api = Api(api_name='v1')

category_resource = CtegoryResource()
product_resource = ProductResource()

api.register(category_resource)
api.register(product_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('api/', include(api.urls)),
]
