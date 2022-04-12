from posts.models import Post
from categories.models import Category, SubCategory
from accounts.models import User
from django.core.cache import cache



def create_process_context():
    context = {}
    
    context['posts'] = Post.objects.filter(published=True).select_related('category')
    context['categories'] = Category.objects.all()
    context['subcategories'] = SubCategory.objects.all()
    context['authors'] = User.objects.filter(posts__gte=1).distinct()
    
    cache_context = { k: v[:].values() for k,v in context.copy().items()}
    update_subcategories_values(cache_context)
    cache.set('context', cache_context, None)
    
    return context


def get_updated_key_value(key: str):
    match key:
        case 'posts':
            return Post.objects.filter(published=True).select_related('category').values()
        case 'categories':
            return Category.objects.all().values()
        case 'subcategories':
            context = SubCategory.objects.all().values()
            update_subcategories_values(context)
            return context
        case 'authors':
            return User.objects.filter(posts__gte=1).distinct().values()
        case _:
            raise ValueError('Invalid key')


def update_process_context():
    updated_obj = cache.get('updated')
    update = all(list(updated_obj.keys()))

    if update:
        context = create_process_context()
        return context, updated_obj
    return {}, updated_obj




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



def update_subcategories_values(cache_obj):
    cache_obj['subcategories'] = [{**subcategory, 'category': cache_obj["categories"].get(id=subcategory["category_id"])["slug"]} for subcategory in cache_obj['subcategories']]
