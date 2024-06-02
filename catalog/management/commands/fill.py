import json
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open('category.json', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('product.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.truncate_table_restart_id()
        Category.objects.all().delete()

        category_list = []
        for category in Command.json_read_categories():
            category_list.append(
                {"id": category['pk'], "category_name": category['fields']['category_name'],
                 "description": category['fields']['description']}
            )

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category.objects.create(**category_item)
            )

        product_list = []
        for product in Command.json_read_products():
            product_list.append(
                {"id": product['pk'],
                 "product_name": product['fields']['product_name'],
                 "description": product['fields']['description'],
                 "price": product['fields']['price'],
                 "category": Category.objects.get(pk=product['fields']['category']),
                 "image_preview": product['fields']['image_preview'],
                 "created_at": product['fields']['created_at'],
                 "updated_ad": product['fields']['updated_ad']}
            )
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product.objects.create(**product_item)
            )

        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)
