from main import get_main_spa, update_main_spa
from django.core.cache import cache



def create_static_pages():
    spa_data = {
        'main': get_main_spa(),
    }
    
    cache.set('SPGT', spa_data)
    
    return {'SPGT': ['main']}



def update_static_pages():
    updated_spa, not_updated_spa  = [], []
    spa_data: dict = cache.get('SPGT')
    new_spa_data = dict()
    
    for spa_name in spa_data.keys():
        response = update_main_spa(spa_data[spa_name])

        if response['updated']:
            new_spa_data[spa_name] = response['spa']
            updated_spa.append({spa_name: response['report']})
        else:
            new_spa_data[spa_name] = spa_data[spa_name]
            not_updated_spa.append(spa_name)
            
    if updated_spa != []:
        cache.set('SPGT', new_spa_data) 
        
    return {'updated': updated_spa, 'not_updated': not_updated_spa}
    