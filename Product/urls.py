from django.urls import path, include
from .views import *

app_name = "Product"
urlpatterns = [
    path('', Product_List.as_view(), name="product_list"),
    path('<pk>/<slug>', Product_Detail.as_view(), name="product_detail"),
    path('search', Product_List_Search.as_view(), name="product_search"),
]