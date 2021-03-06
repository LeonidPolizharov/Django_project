"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('social/', include('social_django.urls', namespace='social')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('orders/', include('ordersapp.urls', namespace='orders')),
    
    path('', mainapp.index, name='index'),
    path('contact/', mainapp.contact, name='contact'),
    path('products/', mainapp.products, name='products'),
    path('products/<int:pk>/', mainapp.category, name='category'),
    path('products/<int:pk>/<int:page>/', mainapp.category, name='category'),
    path('products/<int:pk>/<int:page>/products/', mainapp.category_products, name='category_products'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
