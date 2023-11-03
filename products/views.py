from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.http import Http404


# Create your views here.


def product_detail(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        context = {'product': product}
        return render(request, 'products/product_detail.html', context)
    except Exception as e:
        # return render(Http404)
        print(e)

