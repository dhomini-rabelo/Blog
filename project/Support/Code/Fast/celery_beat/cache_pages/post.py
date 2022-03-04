from django.core.cache import cache


def create_cache_page_for_posts(context):
    data = {}
    for post in context['posts']:
        data[str(post.code)] = {
            'title': post.title,
            'img': post.img.url,
            'text': post.text,
        }
        
    cache.set('cache_page__posts', data, None)