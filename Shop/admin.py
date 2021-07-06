from django.contrib import admin
from .models import Product, ProductCategory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated',)
    list_display = ('name', 'price', 'category', 'availability')
    search_fields = ('name',)
    

class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated',)
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
