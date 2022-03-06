from Support.Code.Fast.models.cards import get_suggestion_html
from suggestions.models import CategorySuggestion, SubCategorySuggestion
from accounts.models import User
from celery import shared_task



@shared_task(name='saving suggestion')
def save_suggestion(suggestion: str, type_: str, email: str):
    user = User.objects.get(email=email)
    
    match type_:
        case 'categories':
            new_suggestion = CategorySuggestion.objects.create(name=suggestion, user=user)
        case 'subcategories':
            new_suggestion = SubCategorySuggestion.objects.create(name=suggestion, user=user)
    
    
    user.my_static_pages['suggestions'][type_] += get_suggestion_html(suggestion, 'loading')
    user.save()
                        
    return {'suggestion': suggestion, 'type': type_, 'user': user.name}
    