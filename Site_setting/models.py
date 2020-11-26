from django.db import models


# Create your models here.

class Site_Setting(models.Model):
    Brand = models.CharField(max_length=150, verbose_name="نام محموعه")
    address = models.CharField(max_length=400, verbose_name="آدرس")
    Phone = models.CharField(max_length=20, verbose_name="تلفن")
    email = models.EmailField(verbose_name="ایمیل")

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "گروه تنظیمات"

    def __str__(self):
        return self.Brand
