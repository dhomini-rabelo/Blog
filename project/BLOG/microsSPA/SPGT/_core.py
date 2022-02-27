from main import get_main_spa
from django.core.cache import cache



def construct_static_pages():
    
    response = cache.get_many(['update_posts', 'update_categories', 'update_authors'])
    
    spa_data = {
        'main': get_main_spa(),
    }
    
    cache.set('SPGT', spa_data)
    
    return {'status': 'success'}