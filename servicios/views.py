from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.


from .models import Servicios


def servicios(request):
    servicios = Servicios.objects.all()

    context = {
        "servicios": servicios
    }

    return render(request, 'servicios/servicios.html', context)
