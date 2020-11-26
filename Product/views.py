from django.shortcuts import render, Http404
from .models import Product
from django.views.generic import ListView, DetailView
from Category.models import ProductCategory
from Brand.models import Product_Brand


# Create your views here.

def Product_Category_Filter(request):
    categories = ProductCategory.objects.all()
    context = {
        'category': categories
    }
    return render(request, 'Product/component/category_items.html', context)


def Product_Brand_Filter(request):
    brand = Product_Brand.objects.all()
    context = {"brands": brand}
    return render(request, 'Product/component/brand_items.html', context)


class Product_List(ListView):
    template_name = 'Product/Product_list.html'
    context_object_name = "objects"
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Product_List, self).get_context_data()
        context["page_title"] = "Product List"
        return context

    def get_queryset(self):
        request = self.request
        return Product.objects.filter(active=True)


class Product_Detail(DetailView):
    template_name = 'Product/Product_detail.html'
    queryset = Product.objects.filter(active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Product_Detail, self).get_context_data()
        context["page_title"] = "Product Detail"
        return context


class Product_List_Search(ListView):
    template_name = 'Product/Product_list.html'
    context_object_name = "objects"
    paginate_by = 12

    def get_queryset(self):
        request = self.request
        qs = request.GET.get('product_page_search')
        if qs is not None:
            return Product.objects.get_search(qs)
        return not Product.objects.none()


class Product_Category(ListView):
    template_name = 'Product/Product_list.html'
    context_object_name = "objects"
    paginate_by = 12

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        query = ProductCategory.objects.filter(name__iexact=category_name).first()
        if query is None:
            raise Http404("صفحه مورد نظر یافت نشد")
        else:
            return Product.objects.get_category(query.name)


class Product_Brand_List(ListView):
    template_name = 'Product/Product_list.html'
    context_object_name = "objects"
    paginate_by = 12

    def get_queryset(self):
        brand_name = self.kwargs["barnd_name"]
        query = Product_Brand.objects.filter(name__iexact=brand_name).first()
        if query is None:
            raise Http404("صفحه مورد نظر یافت نشد")
        return Product.objects.get_brand(query)
