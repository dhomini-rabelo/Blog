from django.urls import path
from .views import *

urlpatterns = [
    path('autores/', AuthorsList.as_view(), name='authors'),
]
