from django.shortcuts import render
from .models import Contact_US
from Site_setting.models import Site_Setting

# Create your views here.

def Contact_Us(request):
    full_name = request.POST.get("full_name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    text = request.POST.get("text")
    if request.method == "POST":
        Contact_US.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
    setting = Site_Setting.objects.first()
    context = {"setting": setting}
    return render(request, 'Contact_Us/contact-us.html', context)
