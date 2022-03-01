from django.shortcuts import render
from django.views.generic import View
from django.core.cache import cache


class LatestPosts(View):
    def get(self, request):
        print(cache.get('search_api'))
        return render(request, 'posts/index.html')


class PostView(View):
    def get(self, request):
        return render(request, 'posts/post.html')



