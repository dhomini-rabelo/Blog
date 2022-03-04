from django.core.cache import cache
from posts.models import Post


def create_post_api_data(context):
    posts_data = {}

    for post in context['posts']:
        posts_data[str(post.code)] = {
            'text': post.text,
            'img': post.img,
        }
        
    cache.set('post_api', posts_data, None)
    
    
    
def update_post_api_data(post_code):
    post = Post.objects.get(code=post_code)
    pass