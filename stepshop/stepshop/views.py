from django.shortcuts import render

from mainapp.models import Product

links_menu = [
    {'href': 'index', 'name': 'Домой', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contact/'},
]


def index(request):
    page_name = 'главная страница'

    products_ = Product.objects.all()

    context = {
        'title': page_name,
        'links_menu': links_menu,
        'products': products_,
    }

    return render(request, "index.html", context)


def about(request):
    page_name = 'о нас'

    context = {
        'title': page_name,
        'links_menu': links_menu,
    }
    return render(request, "about.html", context)


def contact(request):
    page_name = 'контакты'

    context = {
        'title': page_name,
        'links_menu': links_menu,
    }
    return render(request, "contact.html", context)
