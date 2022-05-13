from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
# import json
from .models import Category, Product


MENU_LINKS = {
    'index': 'Главная',
    'products': 'Продукты',
    'contact': 'Контакты',
}


def index(request):
    return render(request, 'mainapp/index.html', context={
      'title': 'Главная',
      'menu': MENU_LINKS,
       })

    
def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    # with open('/products.json', 'r', encoding='utf-8') as f:
    #    products = json.load(f)
    # этот код не удаляю, оставляю для себя, чтобы не забыть про возможность 
    # грузить из файла
    return render(request, 'mainapp/products.html', context={
      'title': 'Продукты',
      'menu': MENU_LINKS,
      'products': products,
      'categories': categories,
      })


def category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category).order_by('price')
    return render(request, 'mainapp/category.html', context={
        'title': 'Продукты',
        'menu': MENU_LINKS,
        'products': products,
        'category': category,
        'categories': categories,
        })
        

def contact(request):
    return render(request, 'mainapp/contact.html', context={
      'title': 'Контакты',
      'menu': MENU_LINKS,
      })
