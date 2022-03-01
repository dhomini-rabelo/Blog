from django.core.cache import cache
from posts.models import Post
from categories.models import Category, SubCategory
from accounts.models import User


def create_search_api_data():
    posts = list(Post.objects.values_list('title', flat=True))
    categories = list(Category.objects.values_list('name', flat=True))
    subcategories = list(SubCategory.objects.values_list('name', flat=True))
    authors = list(User.objects.values_list('name', flat=True))
    
    cache.set('search_api', { 
                
            'posts': posts, 
            'categories': categories,
            'authors': authors,
            'subcategories': subcategories,
            
    }, None)
    



def updated_search_api_data():
    updated_obj = cache.get('updated')
    search_api_data: dict = cache.get('search_api')
    
    if updated_obj['posts']:
        search_api_data['posts'] = Post.objects.values_list('title', flat=True)

    if updated_obj['categories']:
        search_api_data['categories'] = Category.objects.values_list('name', flat=True)

    if updated_obj['subcategories']:
        search_api_data['subcategories'] = SubCategory.objects.values_list('name', flat=True)

    if updated_obj['authors']:
        search_api_data['authors'] = User.objects.values_list('name', flat=True)
    
    
    cache.set('search_api', search_api_data, None)
    
    return {'report': updated_obj, 'search_api_data': search_api_data}