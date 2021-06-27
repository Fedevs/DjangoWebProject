from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50, verbose_name="content")
    image=models.ImageField(upload_to='Blog', null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
