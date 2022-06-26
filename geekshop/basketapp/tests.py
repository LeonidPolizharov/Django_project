from unicodedata import category
from django.test import TestCase
from django.test.client import Client
from mainapp.models import Category, Product
from basketapp.models import Basket
from authapp.models import ShopUser
from authapp.tests import ShopUserFactory


class TestBasketappPages(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category(name='test')
        self.category.save()
        self.product = Product(category=self.category, name='test')
        self.product.save()
        self.user = ShopUserFactory(
            username='user',
            pasword='password'
        )
        self.user.save()

    def test_login_required_for_basket(self):
        response = self.client.get('/basket/')
        self.assertRedirects(response, '/auth/login/?next=%2Fbasket%2F')
        self.assertEqual(response.status_code, 302)


class TestBasketModel(TestCase):

    def test_basket_cost(self):
        category = Category(name='test')
        category.save()
        product = Product(name='test', price=100, category=category)
        product.save()
        user = ShopUser(username='user')
        user.save()
        basket_item = Basket(quantity=10, user=user, product=product)
        basket_item.save()
        self.assertEqual(basket_item.cost, 1000)

