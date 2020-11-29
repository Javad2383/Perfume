from django.db import models
from django.contrib.auth.models import User
from Product.models import Product


# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, null=True, blank=True, verbose_name="پرداخت شده")
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ شداخت')

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید کاربران"

    def __str__(self):
        return self.owner.get_full_name()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")

    class Meta:
        verbose_name = "جزییات محصول"
        verbose_name_plural = "اطلاعات جزییات محصول"

    def __str__(self):
        return self.product.title
