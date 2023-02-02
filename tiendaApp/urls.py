from django.urls import path, include
from . import views
from distutils.log import debug
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
]


# url para servir las imagenes
