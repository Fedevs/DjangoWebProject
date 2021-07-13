from django.shortcuts import render, redirect
from .shopCart import Cart
from Shop.models import Product

# Create your views here.

def add_product(request, id_product):
    cart = Cart(request)
    product = Product.objects.get(id = id_product)
    cart.add(product = product)
    return redirect('Shop')

def delete_product(request, id_product):
    cart = Cart(request)
    product = Product.objects.get(id = id_product)
    cart.delete(product = product)
    return redirect('Shop')

def subtract_product(request, id_product):
    cart = Cart(request)
    product = Product.objects.get(id = id_product)
    cart.subtract(product = product)
    return redirect('Shop')

def clean_cart(request):
    cart = Cart(request)
    cart.clean()
    return redirect('Shop')


