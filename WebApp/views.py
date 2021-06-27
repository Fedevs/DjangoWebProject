from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'WebApp/home.html')

def shop(request):
    return render(request, 'WebApp/shop.html')

def contact(request):
    return render(request, 'WebApp/contact.html')