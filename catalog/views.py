from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('product_name', 'description', 'image_preview', 'category', 'price', 'created_at')
#     success_url = reverse_lazy('catalog:product_catalog')
#
#
# class ProductUpdateView(UpdateView):
#     model = Product
#     fields = ('product_name', 'description', 'image_preview', 'category', 'price', 'created_at')
#     success_url = reverse_lazy('catalog:product_catalog')
#
#     def get_success_url(self):
#         return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})
#
#
# class ProductDeleteView(DeleteView):
#     model = Product
#     success_url = reverse_lazy('catalog:product_catalog')
