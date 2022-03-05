from django.urls import path
from .views import *

urlpatterns = [
    path('autores/', AuthorsListView.as_view(), name='authors'),
    path('autores/<slug:author_slug>', AuthorPostsView.as_view(), name='authors_posts'),
]
