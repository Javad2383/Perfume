from django.shortcuts import render
from django.contrib.auth import login


def Home_Page(request):
    context = {}
    return render(request, 'Pages/fa/index.html', context)
