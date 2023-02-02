from django.contrib import admin
from django.urls import path, include
from distutils.log import debug
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('tiendaApp.urls')),
    path('servicios/', include("servicios.urls")),
    path('blog/', include("blog.urls")),
    path('contacto/', include("contacto.urls")),
    path('tienda/', include("tienda.urls")),
    path('carro/', include("carro.urls")),
    path('autenticacion/', include("autenticacion.urls")),
    path('pedidos/', include("pedidos.urls")),

]


# Para servir las imagenes en desarrollo
# url para servir las imagenes
if debug:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
