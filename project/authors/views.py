from django.shortcuts import render
from django.views.generic import View




class AuthorsList(View):
    def get(self, request):
        return render(request, 'authors/list_authors.html')
