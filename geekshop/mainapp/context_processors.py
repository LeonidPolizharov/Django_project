def menu_links(request):
    return {
        'menu': {
            'index': 'Главная',
            'products': 'Продукты',
            'contact': 'Контакты',
        }
    }
