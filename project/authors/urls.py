from django.urls import path
from .views import *

urlpatterns = [
    path('autores/', AuthorsList.as_view(), name='authors'),
    path('autores/<slug:author_slug>', AuthorView.as_view(), name='authors_posts'),
]
