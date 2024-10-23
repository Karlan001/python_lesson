from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product, Order


# Create your views here.

def myshop(request: HttpRequest):
    products = ['smartphone', 'TV', 'Notebook']
    context = {
        'product': products,
    }
    return render(request, 'myshop/index.html', context=context)

def product_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'myshop/products.html', context=context)

def order_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(request, 'myshop/orders.html', context=context)