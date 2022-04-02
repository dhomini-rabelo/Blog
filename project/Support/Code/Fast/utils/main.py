from django.core.cache import cache


def update_cache_keys(*keys):
    updated_obj = cache.get('updated')
    for key in keys:
        updated_obj[key] = True
    cache.set('updated', updated_obj, None)