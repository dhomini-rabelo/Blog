from posts.models import Post
from categories.models import Category, SubCategory
from accounts.models import User
from django.core.cache import cache



def create_process_context():
    context = {}
    
    context['posts'] = Post.objects.all().select_related('category')
    context['categories'] = Category.objects.all()
    context['subcategories'] = SubCategory.objects.all()
    context['authors'] = User.objects.filter(posts__gte=1).distinct()
    
    cache_context = { k: v[:].values() for k,v in context.copy().items()}
    cache_context['subcategories'] = [{**subcategory, 'category': cache_context["categories"].get(id=subcategory["category_id"])["slug"]} for subcategory in cache_context['subcategories']]
    cache.set('context', cache_context, None)
    return context


def get_updated_key_value(key: str):
    match key:
        case 'posts':
            return list(Post.objects.all().select_related('category').values())
        case 'categories':
            return list(Category.objects.all().values())
        case 'subcategories':
            context = SubCategory.objects.all().values()
            context['subcategories'] = [{**subcategory, 'category': Category.objects.get(slug=subcategory['slug']).slug} for subcategory in context['subcategories']]
            return list(context)
        case 'authors':
            return list(User.objects.filter(posts__gte=1).distinct().values())
        case _:
            raise ValueError('Invalid key')


def update_process_context():
    context = cache.get('context')
    updated_obj = cache.get('updated')
    update = False

    for key in updated_obj.keys():
        if updated_obj.get(key) is True:
            context[key] = get_updated_key_value(key)
            update = True
    
    if update: 
        cache.set('context', context, None)
    return context




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
