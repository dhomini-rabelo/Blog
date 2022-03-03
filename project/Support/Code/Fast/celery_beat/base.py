from posts.models import Post
from categories.models import Category, SubCategory
from accounts.models import User
from django.core.cache import cache



def create_process_context():
    context = {}
    
    context['posts'] = Post.objects.all().select_related('category')
    context['categories'] = Category.objects.all()
    context['subcategories'] = SubCategory.objects.all()
    context['authors'] = User.objects.filter(posts__gte=1)
    
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
