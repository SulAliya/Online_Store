from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation.trans_real import catalog
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'image_preview', 'category', 'price', 'created_at')
    success_url = reverse_lazy('catalog:product_catalog')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'image_preview', 'category', 'price', 'created_at')
    success_url = reverse_lazy('catalog:product_catalog')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_catalog')


