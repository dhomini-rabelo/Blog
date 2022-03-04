from django.core.cache import cache
from Support.Code.Fast.models.cards import get_categories_list_html
from django.utils.html import format_html
from .pages.list_subcategories import html


def create_cache_page_for_list_subcategories(context):
    data = {}
    context_categories = context['categories']
    context_subcategories = context['subcategories']
    
    for category in context_categories:
        subcategories = context_subcategories.filter(category=category)
        subcategories_html = get_categories_list_html(subcategories)
        page_html = html.replace('{{category.name}}', category.name).replace('{{subcategories}}', subcategories_html)
        data[str(category.slug)] = format_html(page_html)
        
    cache.set('cache_page__list_subcategories', data, None)