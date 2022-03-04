from django.core.cache import cache
from Support.Code.Fast.models.cards import get_posts_list_html
from django.utils.html import format_html
from .pages.authors import html


def create_cache_page_for_authors(context):
    data = {}
    
    for author in context['authors']:
        posts = context['posts'].filter(author=author)
        posts_html = get_posts_list_html(posts)
        page_html = html.replace('{{author.name}}', author.name).replace('{{posts}}', posts_html)
        data[str(author.slug)] = format_html(page_html)
        
    cache.set('cache_page__authors', data, None)
