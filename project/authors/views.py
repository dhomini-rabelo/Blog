from django.shortcuts import render
from Support.Code.Fast.StaticPages.SPGT import StaticPageGeneratorByTask



class AuthorsList(StaticPageGeneratorByTask):
    spa_group = 'main'
    spa_page = 'authors'

    def sp_get(self, request):
        return render(request, 'authors/list_authors.html', self.tc)
