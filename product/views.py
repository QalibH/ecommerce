from django.shortcuts import render
from . import Blog

def blog(request):
    return render(request, 'web/home.html')