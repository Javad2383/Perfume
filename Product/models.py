from django.db import models
from django.db.models import Q
from Category.models import ProductCategory
from Brand.models import Product_Brand


# Create your models here.

def image_url(instance, filename):
    return f"product/{instance}/{filename}"


class ProductManager(models.Manager):
    def get_featured(self):
        return self.get_queryset().filter(featured=True)

    def get_search(self, query):
        lookup = (
                Q(tag__title__icontains=query) |
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(slug__icontains=query) |
                Q(brand__name__icontains=query) |
                Q(brand__title__icontains=query) &
                Q(active=True)
        )
        return self.get_queryset().filter(lookup)

    def get_category(self, query):
        return self.get_queryset().filter(active=True, category__name__iexact=query)

    def get_brand(self, query):
        return self.get_queryset().filter(active=True, brand__name__icontains=query)


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to=image_url, verbose_name="عکس")
    price = models.DecimalField(max_digits=50, decimal_places=0, verbose_name="قیمت")
    active = models.BooleanField(default=False, verbose_name="فعال")
    featured = models.BooleanField(default=False, verbose_name="ویژه")
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="Product", unique=True)
    category = models.ManyToManyField(ProductCategory, blank=True, verbose_name="دسته بندی ها")
    brand = models.ManyToManyField(Product_Brand, blank=True, verbose_name="برند")

    objects = ProductManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return f"{self.title}"
