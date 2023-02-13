from django.shortcuts import render
from .models import Blog, Category

# Create your views here.

def blog (request):
    blogs= Blog.objects.all()
    return render(request, "blog/blog.html", {'blogs': blogs})

def category(request, category_id):
    category=Category.objects.get(id=category_id)
    return render(request, "blog/category.html", {'category': category})
