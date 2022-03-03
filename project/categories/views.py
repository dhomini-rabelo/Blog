from django.shortcuts import render
from django.views.generic import View
from Support.Code.Fast.StaticPages.SPGT import StaticPageGeneratorByTask
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator




class CategoriesList(StaticPageGeneratorByTask):
    spa_group = 'main'
    spa_page = 'categories'
    
    def sp_get(self, request):
        return render(request, 'categories/list_categories.html', self.tc)





class SubCategoriesList(View):
    def get(self, request, category):
        return render(request, 'categories/list_subcategories.html')



