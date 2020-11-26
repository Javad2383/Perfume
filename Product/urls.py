from django.urls import path, include
from .views import *

app_name = "Product"
urlpatterns = [
    path('', Product_List.as_view(), name="product_list"),
    path('category-filter', Product_Category_Filter, name="product_category_filter"),
    path('brand-filter', Product_Brand_Filter, name="product_brand_filter"),
    path('product/<pk>/<slug>', Product_Detail.as_view(), name="product_detail"),
    path('search', Product_List_Search.as_view(), name="product_search"),
    path('category/<category_name>', Product_Category.as_view(), name="product_category"),
    path('brand/<barnd_name>', Product_Brand_List.as_view(), name="product_brand"),
]
