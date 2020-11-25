from django.db import models
from Product.models import Product
# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    active = models.BooleanField(default=False)
    product = models.ManyToManyField(Product, blank=True)

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"

    def __str__(self):
        return f"{self.title}"
