from django.shortcuts import render


def products(request):
    page_name = 'продукты'

    context = {
        'title': page_name,
    }
    return render(request, "products.html", context)


def product(request):
    page_name = 'продукт'

    context = {
        'title': page_name,
    }
    return render(request, "product.html", context)
