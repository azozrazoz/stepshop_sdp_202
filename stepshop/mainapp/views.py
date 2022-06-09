from django.shortcuts import render
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Домой', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contact/'},
]


def products(request):
    page_name = 'продукты'

    products_ = Product.objects.all() # .filter(category__name__in=['Джинсы', 'Бобры']).order_by('price')
    categories_ = ProductCategory.objects.all()

    context = {
        'title': page_name,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories_
    }
    return render(request, "products.html", context)


def product(request):
    page_name = 'продукт'

    context = {
        'title': page_name,
        'links_menu': links_menu,
    }
    return render(request, "product.html", context)
