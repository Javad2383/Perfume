from django.shortcuts import render, redirect
from Product.models import Product
from Site_setting.models import Site_Setting
from django.contrib.auth import get_user_model, login, authenticate, logout

User = get_user_model()


def Home_Page(request):
    featured = Product.objects.get_featured()
    news = Product.objects.filter(active=True)
    context = {
        "featured": featured,
        'news': news
    }
    return render(request, 'Pages/fa/index.html', context)


def Header(request):
    settings = Site_Setting.objects.first()
    context = {"setting": settings}
    return render(request, "Layouts/Header.html", context)


def Footer(request):
    settings = Site_Setting.objects.first()
    context = {"setting": settings}
    return render(request, "Layouts/Footer.html", context)


def Register_Page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    context = {}
    if request.method == "POST":
        name = request.POST.get("register_name")
        email = request.POST.get("register_email")
        pass1 = request.POST.get("register_pass_1")
        pass2 = request.POST.get("register_pass_2")
        qs_name = User.objects.filter(username=name)
        qs_email = User.objects.filter(email=email)
        if qs_name.exists():
            context["nameError"] = "نامی که انتخاب کردید در سیستم موجود میباشد"
        elif qs_email.exists():
            context["emailError"] = "ایمیلی که انتخاب کردید در سیستم موجود میباشد"
        elif pass1 != pass2:
            context["passError"] = "پسورد ها باید مثل هم باشند"
        else:
            new_user = User.objects.create_user(username=name, email=email, password=pass1)
            return redirect('home_page')
    return render(request, 'Pages/panel/register.html', context)


def Login_Page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    context = {}
    if request.method == "POST":
        name = request.POST.get('login_name')
        password = request.POST.get('login_pass')
        qs_name = User.objects.filter(username=name)
        if not qs_name.exists():
            context["nameError"] = "نام وارد شده اشتباه است"
        else:
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                context["passError"] = "پسورد اشتباه است"
    return render(request, 'Pages/panel/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login_account')
