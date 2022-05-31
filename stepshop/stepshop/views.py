from django.shortcuts import render


def index(request):
    page_name = 'главная страница'

    context = {
        'title': page_name,
    }

    return render(request, "index.html", context)


def about(request):
    page_name = 'о нас'

    context = {
        'title': page_name,
    }
    return render(request, "about.html", context)


def contact(request):
    page_name = 'о нас'

    context = {
        'title': page_name,
    }
    return render(request, "contact.html")
