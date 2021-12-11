from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', LatestPosts.as_view(), name='latest_posts'),
]
