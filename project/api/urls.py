from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('category-suggestion/view-or-create/<int:user_id>', CategorySuggestionView.as_view(), name='api_category_suggestion'),
    path('subcategory-suggestion/view-or-create/<int:user_id>', CategorySuggestionView.as_view(), name='api_subcategory_suggestion'),
    path('token/get-token', TokenObtainPairView.as_view()),
    path('token/refresh-token', TokenRefreshView.as_view()),
]
