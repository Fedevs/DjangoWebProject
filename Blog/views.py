from django.shortcuts import render
from Blog.models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    categories=Category.objects.all()

    return render(request, 'Blog/blog.html', {'posts': posts, 'categories': categories})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)

    return render(request, 'blog/category.html', {'category': category,'posts': posts})