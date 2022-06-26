from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.conf import settings
import random
from .models import Category, Product


def index(request):
    return render(request, 'mainapp/index.html', context={
      'title': 'Главная',
       })
       

def get_from_cache(key, func):
    if settings.LOW_CACHE:
      value = cache.get(key)
      if not value:
        value = func()
        cache.set(key, value)
      return value
    else:
      return func()


def get_active_categories():
    return get_from_cache(
      'active_categories', 
      lambda: list(Category.objects.all().filter(is_active=True))
    )
    

def products(request):
    categories = get_active_categories()
    products = Product.objects.all().filter(is_active=True)
    hot_product = random.choice(products)
    products = products.exclude(pk=hot_product.pk)
    # with open('/products.json', 'r', encoding='utf-8') as f:
    #    products = json.load(f)
    # этот код не удаляю, оставляю для себя, чтобы не забыть про возможность 
    # грузить из файла
    return render(request, 'mainapp/products.html', context={
      'title': 'Продукты',
      'hot_product': hot_product,
      'products': products,
      'categories': categories,
      })


def product(request, pk):
    categories = get_active_categories()
    product = get_object_or_404(Product, pk=pk)
    return render(
      request, 
      'mainapp/product.html', 
      context={
        'title': product.name,
        'product': product,
        'category': product.category,
        'categories': categories,
      })

def category(request, pk, page=1):
    categories = get_active_categories()
    category = get_object_or_404(Category, id=pk)
      
    return render(request, 'mainapp/category.html', context={
        'title': 'Продукты',
        'category': category,
        'categories': categories,
        'page': page,
        })


@cache_page(3600)
def category_products(request, pk, page=1):
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category).order_by('price')
    paginator = Paginator(products, per_page=3)

    if page > paginator.num_pages:
      return HttpResponseRedirect(reverse('category', args=[category.id]))
      
    return render(request, 'mainapp/includes/category_product_list_inc.html', context={
        'products': paginator.page(page),
        'category': category,
        })
        

def contact(request):
    return render(request, 'mainapp/contact.html', context={
      'title': 'Контакты',
      })
