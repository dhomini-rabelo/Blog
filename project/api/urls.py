from django.urls import path
from .views import *

urlpatterns = [
    path('category-suggestion/view-or-create/<int:user_id>', CategorySuggestionView.as_view(), name='api_category_suggestion'),
    path('subcategory-suggestion/view-or-create/<int:user_id>', CategorySuggestionView.as_view(), name='api_subcategory_suggestion'),
]
