from typing import Any

from django.contrib.auth.decorators import login_required

#! importaciones para login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

# PAGINA PRINCIPAL


@login_required
def index(request):
    return render(request, "venta/index.html")

# ***** PRODUCTOCATEGORIA

# list
# def productocategoria_list(request):
#     categorias = models.ProductoCategoria.objects.all()
#     context = {"object_list": categorias}
#     return render(request, "producto/productocategoria_list.html", context)


class VendedorList(ListView):
    model = models.Vendedor


# create
# def productocategoria_create(request):
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:home")
#     else:
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_form.html", {"form": form})

class VendedorCreate(CreateView):
    model = models.Vendedor
    form_class = forms.VendedorForm
    success_url = reverse_lazy("venta:vendedor_list")


# detail
# def productocategoria_detail(request, pk):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     return render(request, "producto/productocategoria_detail.html", {"object": query})

class VendedorDetail(DetailView):
    model = models.Vendedor

# update
# def productocategoria_update(request, pk):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST, instance=query)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:home")
#     else:
#         form = forms.ProductoCategoriaForm(instance=query)
#     return render(request, "producto/productocategoria_form.html", {"form": form})


class VendedorUpdate(UpdateView):
    model = models.Vendedor
    form_class = forms.VendedorForm
    success_url = reverse_lazy("venta:vendedor_list")


# def productocategoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_confirm_delete.html", {"object": query})

class VendedorDelete(DeleteView):
    model = models.Vendedor
    success_url = reverse_lazy("venta:vendedor_list")


# ***** PRODUCTO

class VentaList(ListView):
    model = models.Venta

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Venta.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Venta.objects.all()
        return object_list


class VentaCreate(CreateView):
    model = models.Venta
    form_class = forms.VentaForm
    success_url = reverse_lazy("venta:venta_list")


class VentaDetail(DetailView):
    model = models.Venta


class VentaUpdate(UpdateView):
    model = models.Venta
    form_class = forms.VentaForm
    success_url = reverse_lazy("venta:venta_list")


class VentaDelete(DeleteView):
    model = models.Venta
    success_url = reverse_lazy("venta:venta_list")