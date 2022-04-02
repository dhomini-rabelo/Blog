from django.core.cache import cache
from posts.models import Post
from categories.models import Category, SubCategory
from accounts.models import User


def create_search_api_data(context):
    posts = list(context['posts'].values_list('title', flat=True))
    categories = list(context['categories'].values_list('name', flat=True))
    subcategories = list(context['subcategories'].values_list('name', flat=True))
    authors = list(context['authors'].values_list('name', flat=True))
    
    cache.set('search_api', { 
                
        'posts': posts, 
        'categories': categories,
        'authors': authors,
        'subcategories': subcategories,
            
    }, None)
    



def update_search_api_data(context, updated_obj):
    search_api_data: dict = cache.get('search_api')
    updated = False
    
    for key in search_api_data.keys():
        if updated_obj[key]:
            updated = True
            search_api_data[key] = update_api_values(key, context)
    
    if updated:
        cache.set('search_api', search_api_data, None)
    
    return {'report': updated_obj, 'search_api_data': search_api_data}


def update_api_values(key, context):
    match key:
        case 'posts':
            return list(context[key].values_list('title', flat=True))
        case 'categories':
            return list(context[key].values_list('name', flat=True))
        case 'subcategories':
            return list(context[key].values_list('name', flat=True))
        case 'authors':
            return list(context[key].values_list('name', flat=True))
        case _:
            raise ValueError('Invalid key')
        