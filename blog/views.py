from django.shortcuts import render
from .models import Post, Categoria


# Create your views here.


def blog(request):

    posts = Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, 'blog/blog.html', context)


def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)

    posts = Post.objects.filter(categorias=categoria)

    context = {
        "categoria": categoria,
        "posts": posts
    }

    return render(request, 'blog/categorias.html', context)
