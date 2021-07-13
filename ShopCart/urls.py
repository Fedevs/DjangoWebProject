from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:id_product>/', views.add_product, name='add'),
    path('delete/<int:id_product>/', views.delete_product, name='delete'),
    path('subtract/<int:id_product>/', views.subtract_product, name='subtract'),
    path('clean/', views.clean_cart, name='clean'),
]

