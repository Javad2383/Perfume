from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "Perfume"
urlpatterns = [
    # Pages
    path('', Home_Page, name="home_page"),
    # Include
    path('products/', include('Product.urls', namespace='Product')),
    # Admin
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
