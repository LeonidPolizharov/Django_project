from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.core.paginator import Paginator
import random
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
    hot_product = random.choice(products)
    products = products.exclude(pk=hot_product.pk)
    # with open('/products.json', 'r', encoding='utf-8') as f:
    #    products = json.load(f)
    # этот код не удаляю, оставляю для себя, чтобы не забыть про возможность 
    # грузить из файла
    return render(request, 'mainapp/products.html', context={
      'title': 'Продукты',
      'menu': MENU_LINKS,
      'hot_product': hot_product,
      'products': products,
      'categories': categories,
      })


def product(request, pk):
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)
    return render(
      request, 
      'mainapp/product.html', 
      context={
        'title': product.name,
        'menu': MENU_LINKS,
        'product': product,
        'category': product.category,
        'categories': categories,
      })

def category(request, pk, page=1):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category).order_by('price')
    paginator = Paginator(products, per_page=3)

    if page > paginator.num_pages:
      return HttpResponseRedirect(reverse('category', args=[category.id]))
      
    return render(request, 'mainapp/category.html', context={
        'title': 'Продукты',
        'menu': MENU_LINKS,
        'products': paginator.page(page),
        'category': category,
        'categories': categories,
        })
        

def contact(request):
    return render(request, 'mainapp/contact.html', context={
      'title': 'Контакты',
      'menu': MENU_LINKS,
      })
