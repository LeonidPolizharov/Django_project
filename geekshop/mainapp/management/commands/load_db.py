from django.core.management.base import BaseCommand
import json
from django.conf import settings
from mainapp.models import Category, Product
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

class Command(BaseCommand):
    def handle(self, *args,**kwargs):
        with open(settings.DATA_ROOT / "categories.json", 'r', encoding='utf-8') as file:
            categories = json.load(file)
            for category_data in categories:
                try:
                    category = Category(**category_data)
                    category.save()
                except IntegrityError:
                    pass

        
        with open(settings.DATA_ROOT / "products.json", 'r', encoding='utf-8') as file:
            products = json.load(file)
            for product_data in products:
                product_data['category'] = Category.objects.get(name=product_data['category'])
                product = Product(**product_data)
                product.save()


        User = get_user_model()
        if not User.objects.filter(username='admin'):
            User.objects.create_superuser(username='admin', password='adminadmin')