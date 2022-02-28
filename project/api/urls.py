from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.suggestions import CategorySuggestionView, SubCategorySuggestionView
from .views.token import get_cookie
from .views.search import SearchApiView

urlpatterns = [
    path('category-suggestion/view-or-create', CategorySuggestionView.as_view()),
    path('subcategory-suggestion/view-or-create', SubCategorySuggestionView.as_view()),
    path('token/get-token', TokenObtainPairView.as_view()),
    path('token/refresh-token', TokenRefreshView.as_view()),
    path('token/get-cookie', get_cookie),
    path('search', SearchApiView.as_view()),
]
