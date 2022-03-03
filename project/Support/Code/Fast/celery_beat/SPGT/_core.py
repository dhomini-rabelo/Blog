from .main import get_main_spa, update_main_spa
from django.core.cache import cache



def create_static_pages(context):
    spa_data = {
        'main': get_main_spa(context),
    }
    
    cache.set('SPGT', spa_data, None)
    



def update_static_pages():
    updated_obj = cache.get('updated')
    new_updated_obj = dict()
    updated_spa, not_updated_spa  = [], []
    spa_data: dict = cache.get('SPGT')
    new_spa_data = dict()
    
    for spa_name in spa_data.keys():
        response = update_spa(spa_name, spa_data[spa_name], updated_obj)

        if response['updated']:
            new_spa_data[spa_name] = response['spa']
            updated_spa.append({spa_name: response['report']})
            for spa_component in response['report']:
                if spa_component in updated_obj.keys():
                    new_updated_obj[spa_component] = True
        else:
            new_spa_data[spa_name] = spa_data[spa_name]
            not_updated_spa.append(spa_name)
            
    if updated_spa != []:
        cache.set_many({
            
            'SPGT': new_spa_data,
            'updated': {
                **updated_obj,
                **new_updated_obj,
            }

        })
        cache.touch('SPGT', None)
        cache.touch('updated', None)
        
    return {'updated': updated_spa, 'not_updated': not_updated_spa}



def update_spa(key, *args):
    match key:
        case 'main':
            return update_main_spa(*args)