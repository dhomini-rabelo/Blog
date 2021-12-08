from django import template


register = template.Library()


@register.filter(name='enumerate')
def _enumerate(iterable):
    return enumerate(iterable)


@register.filter(name='next')
def _next(obj):
    return next(obj)


@register.filter(name='get_item')
def _get_item(obj, index):
    return obj[index]


@register.filter(name='str')
def _str(obj):
    return str(obj)
