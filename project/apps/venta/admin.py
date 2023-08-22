from django.contrib import admin

# Register your models here.
from . import models
admin.site.site_title = "Ventas"



@admin.register(models.Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "celular",
        "avatar"
    )
    list_display = ("usuario","celular","avatar",)
    list_filter = ("usuario",)
    search_fields = ("usuario","celular","avatar",)
    ordering = ("usuario",)



@admin.register(models.Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        "vendedor",
        "producto",
        "cantidad",
        "precio_total",
        "cliente",
        "fecha_venta"
    )
    list_display_links = ("producto",)
    search_fields = ("producto.nombre", "vendedor")
    list_filter = ("vendedor",)
    date_hierarchy = "fecha_venta"