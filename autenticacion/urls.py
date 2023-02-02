from django.urls import path
from .views import Registro, cerrar_sesion,inicio_sesion

urlpatterns = [
    path("", Registro.as_view(), name="registro"),
    path("logout", cerrar_sesion, name="logout"),
    path("login", inicio_sesion, name="login"),


]
