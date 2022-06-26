from itertools import product
from urllib import response
from django.test import TestCase
from django.test.client import Client
from mainapp.models import Category, Product

class TestMainappPages(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category(name='test')
        self.category.save()
        self.product = Product(category=self.category, name='test')
        self.product.save()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('<title>Главная</title>', response.content.decode('utf-8'))

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_products_page(self):
        response = self.client.get('/products', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_category_page(self):
        response = self.client.get(f'/products/{self.category.pk}/', follow=True)
        self.assertEqual(response.status_code, 200)