from django.urls import path
from .views import *

urlpatterns = [
    path('categorias/', CategoriesList.as_view(), name='categories'),
]
