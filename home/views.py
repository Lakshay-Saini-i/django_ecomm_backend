from django.shortcuts import render
from django.http import response, HttpResponse
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'home/index.html', context)