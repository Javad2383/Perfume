from django.contrib import admin
from .models import Contact_US


# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "is_read")
    list_filter = ["is_read"]
    search_fields = ("full_name", "email", "subject")

    class Meta:
        model = Contact_US


admin.site.register(Contact_US, contactAdmin)
