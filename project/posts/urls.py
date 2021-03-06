from django.urls import path
from .views import *

urlpatterns = [
    path('', LatestPostsView.as_view(), name='latest_posts'),
    path('posts/post/<int:code>', PostView.as_view(), name='post'),
    path('posts/post/preview/<int:code>', PostPreview.as_view(), name='post_preview'),
]
