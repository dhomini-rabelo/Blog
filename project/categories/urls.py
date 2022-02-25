from django.urls import path
from .views import *

urlpatterns = [
    path('categorias/', CategoriesList.as_view(), name='categories'),
    path('categorias/<slug:category>/subcategorias/', SubCategoriesList.as_view(), name='subcategories'),
]
