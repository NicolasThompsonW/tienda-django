from django.contrib import admin

# Register your models here.

from .models import CategoriaProd, Producto

# Register your models here.


class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update',)


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update',)


admin.site.register(Producto, ProductoAdmin)

admin.site.register(CategoriaProd, CategoriaProdAdmin)
