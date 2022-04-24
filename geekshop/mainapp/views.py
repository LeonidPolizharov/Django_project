from django.shortcuts import render
import json

MENU_LINKS = {
    'index': 'Главная',
    'products': 'Продукты',
    'contact': 'Контакты',
}

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu': MENU_LINKS,
         })

    
def products(request):
    with open('E:/Django_project/geekshop/products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu': MENU_LINKS,
        'products': products
        })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu': MENU_LINKS,
        })
