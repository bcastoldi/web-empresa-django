from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all() # recupero todos los posts
    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id): # category_id sera el primary key, es el numero interno que se crea automaticamente que diferencia todas las "filas" de las tablas (registros de la BBDD)
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category': category})
