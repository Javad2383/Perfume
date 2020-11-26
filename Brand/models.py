from django.db import models

# Create your models here.


class Product_Brand(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name =  models.CharField(max_length=150, verbose_name='نام در url')

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برند ها"

    def __str__(self):
        return self.name