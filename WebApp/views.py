from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HOME")

def services(request):
    return HttpResponse("SERVICES")

def shop(request):
    return HttpResponse("SHOP")

def blog(request):
    return HttpResponse("BLOG")

def contact(request):
    return HttpResponse("contact")