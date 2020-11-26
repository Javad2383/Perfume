from django.shortcuts import render
from Product.models import Product
from Site_setting.models import Site_Setting


def Home_Page(request):
    featured = Product.objects.get_featured()
    context = {
        "featured": featured,
    }
    return render(request, 'Pages/fa/index.html', context)


def Header(request):
    settings = Site_Setting.objects.first()
    context = {"setting": settings}
    return render(request, "Layouts/Header.html", context)


def Footer(request):
    settings = Site_Setting.objects.first()
    context = {"setting": settings}
    return render(request, "Layouts/Footer.html", context)
