from django.contrib import admin
from .models import ProductCategory


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name")
    search_fields = ("name", "__str__")

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory)
