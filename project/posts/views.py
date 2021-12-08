from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


BP = 'posts'


class LatestPosts(View):
    def get(self, request):
        return render(request, f'{BP}/index.html')

