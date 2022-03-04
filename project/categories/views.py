from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from Support.Code.Fast.StaticPages.SPGT import StaticPageGeneratorByTask
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from Support.Code.actions.Support.django.views import BaseView



class CategoriesList(StaticPageGeneratorByTask):
    spa_group = 'main'
    spa_page = 'categories'
    
    def sp_get(self, request):
        return render(request, 'categories/list_categories.html', self.tc)





class SubCategoriesList(BaseView):
    def get(self, request, category_slug): 
        print('oi')
        list_subcategories = cache.get('cache_page__list_subcategories')
        subcategories = list_subcategories.get(str(category_slug))
        print(list_subcategories)
        print(subcategories)
        if subcategories is None: raise Http404
        self.tc['subcategories'] = subcategories
        return render(request, 'categories/list_subcategories.html', self.tc)




class SubCategoriesView(BaseView):
    def get(self, request, subcategory_slug):
        subcategory_posts = cache.get('cache_page__subcategories')
        posts = subcategory_posts.get(str(subcategory_slug))
        if posts is None: raise Http404
        self.tc['posts'] = posts
        return render(request, 'categories/subcategory_posts.html', self.tc)