from django.core.cache import cache


def create_base():
    cache.set('updated', {
        'posts': False,
        'categories': False,
        'subcategories': False,
        'authors': False,
    })
    
    return {'status': 'success'}