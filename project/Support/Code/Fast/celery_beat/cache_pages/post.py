from django.core.cache import cache
from django.utils.html import format_html
from .pages.posts import html

def create_cache_page_for_posts(context):
    data = {}
    for post in context['posts']:
        if post.published:
            post_html = html.replace('{{title}}', post.title).replace('{{text}}', post.text).replace('{{img}}', post.img.url)
            data[str(post.code)] = format_html(post_html)
        
    cache.set('cache_page__posts', data, None)