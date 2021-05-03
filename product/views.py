from django.shortcuts import render


def product_list(request):
    context = {
        'title': 'Product list',
        'Products': [
            {"title": "Product #1", "url": "product-1"},
            {"title": "Product #2", "url": "product-2"},
            {"title": "Product #3", "url": "product-3"},
            {"title": "Product #4", "url": "product-4"},
            {"title": "Product #5", "url": "product-5"},
            {"title": "Product #6", "url": "product-6"},
            {"title": "Product #7", "url": "product-7"},
            {"title": "Product #8", "url": "product-8"},
            {"title": "Product #9", "url": "product-9"},
        ], }

    return render(request, "product.html", context)


def product_detail(request, product_slug):
    return render(request, "product_detail.html", {"product_slug": product_slug})
