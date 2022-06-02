import json
import os.path

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.core import management

from mainapp.models import ProductCategory, Product


JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('flush', verbosity=0, interactive=False)

        categories = load_from_json('categories')
        products = load_from_json('products')

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        for product in products:
            category_pk = product.get['category']
            _category = ProductCategory.objects.get(pk=category_pk)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        User.objects.create_superuser('admin', 'admin@stepshop.kz', '123')
