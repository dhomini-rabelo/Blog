from django.core.cache import cache


def create_cache_initial_data():
    cache.set_many({
        
        'updated': {
            'posts': False,
            'categories': False,
            'subcategories': False,
            'authors': False,
        },
        
        'searches': {}    

    })
    
    cache.touch('updated', None)
    cache.touch('searches', None)
    