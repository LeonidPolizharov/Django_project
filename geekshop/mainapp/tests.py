from itertools import product
from urllib import response
from django.test import TestCase
from django.test.client import Client
from mainapp.models import Category, Product

class TestMainappPages(TestCase):

    def setUp(self):
        self.client = Client()
        category = Category(name='test')
        category.save()
        product = Product(category=category, name='test')
        product.save()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_products_page(self):
        response = self.client.get('/products', follow=True)
        self.assertEqual(response.status_code, 200)
