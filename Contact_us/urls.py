from django.urls import path
from .views import Contact_Us

app_name = "ContactUs"
urlpatterns = [
    path('contact-us/', Contact_Us, name="contact_us")
]