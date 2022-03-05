from django.urls import path
from .views import *

urlpatterns = [ 
    path('categorias/', CategoriesListView.as_view(), name='categories'),
    path('categorias/<str:category_slug>/subcategorias/', SubCategoriesListView.as_view(), name='list_subcategories'),
    path('categorias/subcategorias/<slug:subcategory_slug>', SubCategoriesView.as_view(), name='subcategories'),
]
