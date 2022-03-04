from django.http import Http404
from django.shortcuts import render
from Support.Code.Fast.StaticPages.SPGT import StaticPageGeneratorByTask
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.core.cache import cache
from django.utils.html import format_html
from Support.Code.actions.Support.django.views import BaseView


class AuthorsList(StaticPageGeneratorByTask):
    spa_group = 'main'
    spa_page = 'authors'

    def sp_get(self, request):
        return render(request, 'authors/list_authors.html', self.tc)



class AuthorView(BaseView):
    def get(self, request, author_slug):
        authors_posts = cache.get('cache_page__authors')
        posts = authors_posts.get(str(author_slug))
        if posts is None: raise Http404
        print(posts)
        self.tc['posts'] = posts
        return render(request, 'authors/author_posts.html', self.tc)
    
