from django.urls import path
from .views import *

urlpatterns = [
    path('', LatestPosts.as_view(), name='latest_posts'),
]