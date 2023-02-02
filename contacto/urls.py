
from django.urls import path, include

from .views import contacto

urlpatterns = [
    path('', contacto, name="contacto")
]
