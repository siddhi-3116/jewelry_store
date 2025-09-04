from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    featured_products = Product.objects.filter(in_stock=True)[:8]
    return render(request, 'products/home.html', {'featured_products': featured_products})

def product_list(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, in_stock=True)
    return render(request, 'products/product_detail.html', {'product': product})