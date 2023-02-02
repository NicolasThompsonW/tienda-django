from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    #request.session.flush()

    return render(request, 'tiendaApp/home.html')


"""  print(request.session.items())
    carro = request.session.get('carro')
    if not carro:
        carro = request.session['carro'] = {}
    carro[0] = {
        "nombre": "nico",
        "blablabla": "fnas"
    }
    print(request.session.items())
    del carro[0]["nombre"]
    request.session.flush()
    print(request.session.items())
"""
