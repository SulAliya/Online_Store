from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_catalog, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_catalog, name='product_catalog'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts')

]
