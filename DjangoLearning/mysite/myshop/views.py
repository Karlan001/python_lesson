from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest
from .models import Product, Order
from .forms import CreateProductForm


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


def create_products(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            url = reverse("myshop:product_list")
            return redirect(url)
    else:
        form = CreateProductForm()
    context = {
        'form': form,
    }
    return render(request, 'myshop/create_product.html', context=context)


def order_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(request, 'myshop/orders.html', context=context)
