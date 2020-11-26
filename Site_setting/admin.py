from django.contrib import admin
from .models import Site_Setting
# Register your models here.


class SettingAdmin(admin.ModelAdmin):
    list_display = ("Brand", "Phone", "email")


admin.site.register(Site_Setting, SettingAdmin)