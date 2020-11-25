from django.contrib import admin
from .models import Tag


# Register your models here.


class AdminList(admin.ModelAdmin):
    list_display = (
        "__str__",
        "title"
    )
    search_fields = ("title", "__str_")


admin.site.register(Tag, AdminList)
