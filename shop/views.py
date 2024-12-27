from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import FormRequest, Product
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def contacts(request):
    return render(request, 'shop/contacts.html')

def formRequest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        FormRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        return HttpResponseRedirect(reverse('shop:contacts'))

    return render(request, 'shop/formRequest.html')

def requests(request):
    reqs = FormRequest.objects.all()
    
    return render(request, 'shop/requests.html', {'requests': reqs})

def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'shop/product.html', {'product': product})
    except Product.DoesNotExist:
        raise Http404()