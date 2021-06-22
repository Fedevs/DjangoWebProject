from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'WebApp/home.html')

def services(request):
    return render(request, 'WebApp/services.html')

def shop(request):
    return render(request, 'WebApp/shop.html')

def blog(request):
    return render(request, 'WebApp/blog.html')

def contact(request):
    return render(request, 'WebApp/contact.html')