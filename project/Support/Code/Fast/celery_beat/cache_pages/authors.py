from django.core.cache import cache
from Support.Code.Fast.models.main import show_date



def create_cache_page_for_authors(context):
    data = {}
    
    for author in context['authors']:
        posts = context['posts'].filter(author=author)
        data[str(author.slug)] = [{
            'title': post.title,
            'description': post.description,
            'category': post.category,
            'date': show_date(post.date),
        } for post in posts]
        
    cache.set('cache_page__authors', data, None)
