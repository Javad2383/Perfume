from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView


# Create your views here.


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
