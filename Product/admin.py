from django.contrib import admin
from .models import Product
# Register your models here.


class AdminManager(admin.ModelAdmin):
    list_display = (
        "__str__",
        "title",
        "price",
        'active'
    )
    search_fields = ("title", "price",)
    list_filter = ("title", "active")


admin.site.register(Product, AdminManager)
