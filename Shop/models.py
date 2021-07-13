from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class ProductCategory(models.Model):
    name=models.CharField(max_length=50, verbose_name='Name')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Product Category"
        verbose_name_plural="Product Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50, verbose_name='Name')
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="shop", null=True, blank=True)
    availability=models.BooleanField(default=True)
    price=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"