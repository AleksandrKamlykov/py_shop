from shop.models import Category, Product
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .authentication import CustomApiKeyAuthentication


class CtegoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']
      

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomApiKeyAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

        # def dehydrate_title(self, bundle):
        #     return bundle.data['title'].upper()