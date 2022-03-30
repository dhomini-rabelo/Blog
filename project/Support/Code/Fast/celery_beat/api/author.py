from django.core.cache import cache
from Support.Code.Fast.models.main import show_date



def create_author_api_data(context):
    data = {}
    
    for author in context['authors']:
        posts = context['posts'].filter(author=author)
        data[str(author.slug)] = [{
            'title': post.title,
            'img': post.img.url,
            'description': post.description,
            'category': post.category.name,
            'created': show_date(post.created),
            'code': post.code,
        } for post in posts]
        
    cache.set('author_api', data, None)