from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView



class LatestPosts(View):
    def get(self, request):
        return render(request, 'posts/index.html')


class PostView(View):
    def get(self, request):
        return render(request, 'posts/post.html')



