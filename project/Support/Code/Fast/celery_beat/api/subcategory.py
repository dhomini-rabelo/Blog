from django.core.cache import cache
from Support.Code.Fast.models.main import show_date



def create_subcategory_api_data(context):
    data = {}
    
    for subcategory in context['subcategories']:
        posts = context['posts'].filter(sub_categories__id=subcategory.id)
        data[str(subcategory.slug)] = [{
            'title': post.title,
            'img': post.img.url,
            'description': post.description,
            'category': post.category.name,
            'created': show_date(post.created),
            'code': post.code,
        } for post in posts]
        
    cache.set('subcategory_api', data, None)