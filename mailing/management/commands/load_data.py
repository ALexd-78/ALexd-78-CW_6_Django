import json

from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        # удаление данных из таблицы Category
        Category.objects.all().delete()
        # удаление данных из таблицы Product
        Product.objects.all().delete()

        # наполнение таблицы Category из json-файла
        call_command('loaddata', 'catalog_category.json')
        # наполнение таблицы Product из json-файла
        call_command('loaddata', 'catalog_product.json')

