from django.core.cache import cache


def create_cache_page_for_list_subcategories(context):
    data = {}
    context_categories = context['categories']
    context_subcategories = context['subcategories']
    
    for category in context_categories:
        subcategories = context_subcategories.filter(category=category)
        data[category.name] = [{'name': subcategory.name, 'img': subcategory.img.url} for subcategory in subcategories]
        
    cache.set('cache_page__list_subcategories', data, None)