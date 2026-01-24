from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    category = None
    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)

    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'category': category,
    }

    return render(request, 'store/store.html', context)
