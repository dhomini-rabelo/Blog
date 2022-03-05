from django.http import Http404
from django.shortcuts import render
from Support.Code.Fast.StaticPages.SPGT import GroupSpa, GroupChildrenSpa
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.core.cache import cache
from django.utils.html import format_html
from Support.Code.actions.Support.django.views import BaseView


class AuthorsListView(GroupSpa):
    spa_group = 'main'
    spa_page = 'authors'

    def sp_get(self, request):
        return render(request, 'authors/list_authors.html', self.tc)



class AuthorPostsView(GroupChildrenSpa):
    def sp_get(self, request, author_slug):
        authors_posts = cache.get('cache_page__authors')
        page = authors_posts.get(str(author_slug))
        if page is None: raise Http404
        self.tc['current_cache_page'] = page
        return render(request, 'authors/author_posts.html', self.tc)
    
