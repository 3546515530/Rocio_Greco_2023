from django.urls import path

from . import views

app_name = "venta"

urlpatterns = [path("", views.index, name="home")]

# PRODUCTOCATEGORIA
urlpatterns += [
    path("vendedor/list/", views.VendedorList.as_view(), name="vendedor_list"),
    path("vendedor/create/", views.VendedorCreate.as_view(), name="vendedor_create"),
    path("vendedor/detail/<int:pk>", views.VendedorDetail.as_view(), name="vendedor_detail"),
    path("vendedor/update/<int:pk>", views.VendedorUpdate.as_view(), name="vendedor_update"),
    path("vendedor/delete/<int:pk>", views.VendedorDelete.as_view(), name="vendedor_delete"),
]

# PRODUCTO
urlpatterns += [
    path("venta/list/", views.VentaList.as_view(), name="venta_list"),
    path("venta/create/", views.VentaCreate.as_view(), name="venta_create"),
    path("venta/detail/<int:pk>", views.VentaDetail.as_view(), name="venta_detail"),
    path("venta/update/<int:pk>", views.VentaUpdate.as_view(), name="venta_update"),
    path("venta/delete/<int:pk>", views.VentaDelete.as_view(), name="venta_delete"),
]