from django.shortcuts import render, get_object_or_404
from django.utils.translation.trans_real import catalog
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product

class ProductListView(ListView):
    model = Product
    #app_name/<model_name>_<action>
    #catalog/product_list.html

#
# def home(request):
#     return render(request, 'base.html')
# def product_catalog(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('datas.txt', "w") as file:
            file.write(f'{name}, {phone}, {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)
