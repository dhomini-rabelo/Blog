from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from Support.Code.Fast.StaticPages.SPGT import GroupSpa, GroupChildrenSpa
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from Support.Code.actions.Support.django.views import BaseView



class CategoriesListView(GroupSpa):
    spa_group = 'main'
    spa_page = 'categories'
    
    def sp_get(self, request):
        return render(request, 'categories/list_categories.html', self.tc)





class SubCategoriesListView(GroupChildrenSpa):
    def sp_get(self, request, category_slug): 
        list_subcategories = cache.get('cache_page__list_subcategories')
        page = list_subcategories.get(str(category_slug))
        if page is None: raise Http404
        self.tc['current_cache_page'] = page
        return render(request, 'categories/list_subcategories.html', self.tc)




class SubCategoriesView(GroupChildrenSpa):
    def sp_get(self, request, subcategory_slug):
        subcategory_posts = cache.get('cache_page__subcategories')
        page = subcategory_posts.get(str(subcategory_slug))
        if page is None: raise Http404
        self.tc['current_cache_page'] = page
        return render(request, 'categories/subcategory_posts.html', self.tc)