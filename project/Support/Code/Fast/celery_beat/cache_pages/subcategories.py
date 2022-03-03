from django.core.cache import cache
from Support.Code.Fast.models.main import show_date



def create_cache_page_for_subcategories(context):
    data = {}
    
    for subcategory in context['subcategories']:
        posts = context['posts'].filter(sub_categories__contains=subcategory)
        data[str(subcategory.slug)] = [{
            'title': post.title,
            'description': post.description,
            'category': post.category,
            'date': show_date(post.date),
        } for post in posts]
        
    cache.set('cache_page__subcategories', data, None)