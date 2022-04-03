from django.core.cache import cache
from posts.models import Post
from categories.models import Category, SubCategory
from accounts.models import User


map_posts = lambda context: list(map(lambda post: {
    'title': post.title,
    'img': post.img.url, 
    'url': f'/posts/post/{post.code}',
}, context['posts']))


map_categories = lambda context: list(map(lambda category: {
    'title': category.name,
    'img': category.img.url,
    'url': f'/categorias/{category.slug}/subcategorias',
}, context['categories']))

map_subcategories = lambda context: list(map(lambda subcategory: {
    'title': subcategory.name,
    'img': subcategory.img.url,
    'url': f'categorias/subcategorias/{subcategory.slug}',
}, context['subcategories']))

map_authors = lambda context: list(map(lambda author: {
    'title': author.name,
    'img': author.photo.url,
    'url': f'/autores/{author.slug}',
}, context['authors']))



def create_search_api_data(context):
    posts = map_posts(context)
    categories = map_categories(context)
    subcategories = map_subcategories(context)
    authors = map_authors(context)
    
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
            return map_posts(context)
        case 'categories':
            return map_categories(context)
        case 'subcategories':
            return map_subcategories(context)
        case 'authors':
            return map_authors(context)
        case _:
            raise ValueError('Invalid key')
        