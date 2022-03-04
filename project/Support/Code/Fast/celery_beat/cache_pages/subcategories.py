from django.core.cache import cache
from Support.Code.Fast.models.cards import get_posts_list_html
from django.utils.html import format_html
from .pages.subcategories import html



def create_cache_page_for_subcategories(context):
    data = {}
    
    for subcategory in context['subcategories']:
        posts = context['posts'].filter(sub_categories__id=subcategory.id)
        posts_html = get_posts_list_html(posts)
        page_html = html.replace('{{subcategory.name}}', subcategory.name).replace('{{posts}}', posts_html)
        data[str(subcategory.slug)] = format_html(page_html)
        
    cache.set('cache_page__subcategories', data, None)