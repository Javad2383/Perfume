from django.db import models
from django.db.models import Q
from Category.models import ProductCategory

# Create your models here.

def image_url(instance, filename):
    return f"product/{instance}/{filename}"


class ProductManager(models.Manager):
    def get_search(self, query):
        lookup = (
                Q(tag__title__icontains=query) |
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(slug__icontains=query)
                  )
        return self.get_queryset().filter(lookup, active=True)


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to=image_url, verbose_name="عکس")
    price = models.DecimalField(max_digits=50, decimal_places=0, verbose_name="قیمت")
    active = models.BooleanField(default=False, verbose_name="فعال")
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="Product")
    category = models.ManyToManyField(ProductCategory, blank=True, verbose_name="دسته بندی ها")

    objects = ProductManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return f"{self.title}"
