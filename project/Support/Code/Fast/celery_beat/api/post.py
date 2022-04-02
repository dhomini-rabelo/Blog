from django.core.cache import cache
from posts.models import Post


def create_post_api_data(context):
    posts_data = {}

    for post in context['posts']:
        posts_data[str(post.code)] = {
            'text': post.text,
            'img': post.img.url,
        }
        
    cache.set('post_api', posts_data, None)
    
    
