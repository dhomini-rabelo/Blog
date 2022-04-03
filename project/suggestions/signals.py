from django.db.models.signals import post_save
from Support.Code.Fast.models.cards import get_suggestions_list_html
from .models import CategorySuggestion, SubCategorySuggestion



def update_suggestions_html(sender, instance, created, **kwargs):
    user = instance.user

    if isinstance(instance, CategorySuggestion):
        type_ = 'categories'
        suggestions = CategorySuggestion.objects.filter(user=user)
    elif isinstance(instance, SubCategorySuggestion):
        type_ = 'subcategories'
        suggestions = SubCategorySuggestion.objects.filter(user=user)
    else:
        raise ValueError('Instance type not found')
        
    base = user.my_static_pages
    suggestions_html = get_suggestions_list_html(suggestions)
    base['suggestions'][type_] = suggestions_html
    user.my_static_pages = base.copy()
    user.save()




post_save.connect(update_suggestions_html, sender=CategorySuggestion)
post_save.connect(update_suggestions_html, sender=SubCategorySuggestion)