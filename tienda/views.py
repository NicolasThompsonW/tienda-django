from django.shortcuts import render

from .models import Producto, CategoriaProd


def tienda(request):

    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()

    context = {
        "productos": productos,
        "categorias": categorias
    }
    print(request.session.items())

    return render(request, 'tienda/tienda.html', context)
