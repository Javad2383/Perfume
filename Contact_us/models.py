from django.db import models

# Create your models here.


class Contact_US(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=100)
    text = models.TextField()
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس های کاربران"

    def __str__(self):
        return self.email