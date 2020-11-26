from django.contrib import admin
from .models import Product_Brand


# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title")
    search_fields = ("__str__", "title")

    class Meta:
        model = Product_Brand

admin.site.register(Product_Brand, BrandAdmin)
