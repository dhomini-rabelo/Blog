from django.shortcuts import render
from django.views.generic import View
from Support.Code.Fast.StaticPages.SPGT import StaticPageGeneratorByTask
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator




@method_decorator(cache_page(60 * 5))
class LatestPosts(StaticPageGeneratorByTask):
    spa_group = 'main'
    spa_page = 'posts'
    
    def sp_get(self, request):
        return render(request, 'posts/index.html', self.tc)


class PostView(View):
    def get(self, request):
        return render(request, 'posts/post.html')



 