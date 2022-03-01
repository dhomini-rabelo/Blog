from celery import shared_task
from ..models import User
from posts.models import Post
from suggestions.models import SubCategorySuggestion, CategorySuggestion
from Support.Code.Fast.models.cards import get_posts_list_html, get_suggestions_list_html



@shared_task(name='USPGT_update_my_posts_list')
def update_posts_list(email: str, published: bool):
    user = User.objects.get(email=email)
    my_posts = Post.objects.filter(user__email=email).exclude(published=published).select_related('category')
    process = 'posts_list' if published else 'drafts_list'

    html = get_posts_list_html(my_posts)
    new_my_static_pages = user.my_static_pages.copy()
    new_my_static_pages['post'][process] = html
    
    user.my_static_pages = new_my_static_pages
    user.save()
    
    return {f'update_{process}': email}



@shared_task(name='USPGT_update_my_suggestions_list')
def update_suggestions(email:str, suggestion_type:str):
    user = User.objects.get(email=email)

    match suggestion_type:
        case 'categories':
            suggestions = CategorySuggestion.objects.filter(user__email=email)
        case 'subcategories':
            suggestions = SubCategorySuggestion.objects.filter(user__email=email)
        case _:
            raise ValueError('Invalid suggestion type')
        
    html = get_suggestions_list_html(suggestions)
    new_my_static_pages = user.my_static_pages.copy()
    new_my_static_pages['suggestions'][suggestion_type] = html
    
    user.my_static_pages = new_my_static_pages
    user.save()
    
    return {f'update_{suggestion_type}': email}
    