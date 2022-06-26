from django.test import TestCase
from factory.django import DjangoModelFactory


class ShopUserFactory(DjangoModelFactory):
    class Mets:
        model = 'authapp.ShopUser'