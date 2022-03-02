from django.shortcuts import render
from Support.Code.Fast.StaticPages.SPGT import StaticPageGeneratorByTask
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator




# @method_decorator(cache_page(60 * 5))
class AuthorsList(StaticPageGeneratorByTask):
    spa_group = 'main'
    spa_page = 'authors'

    def sp_get(self, request):
        return render(request, 'authors/list_authors.html', self.tc)
