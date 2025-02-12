from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.views.generic import DetailView


class MyClass(View):
    def get(self, request):
        return HttpResponse('views from the class based view')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'cbv/product_form.html'
    # Redirect to product list after successful creation
    success_url = reverse_lazy('cbv:product-list')


class ProductListView(ListView):
    model = Product
    template_name = 'cbv/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'cbv/product_detail.html'
    context_object_name = 'product'
    slug_field = 'prodname'  # Field to use for lookup
    slug_url_kwarg = 'name'  # URL parameter name


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'cbv/product_confirm_delete.html'
    success_url = reverse_lazy('cbv:product-list')
