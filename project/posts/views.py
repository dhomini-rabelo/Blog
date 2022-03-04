from django.http import Http404
from django.shortcuts import render
from Support.Code.Fast.StaticPages.SPGT import StaticPageGeneratorByTask
from django.core.cache import cache
from django.utils.html import format_html
from Support.Code.actions.Support.django.views import BaseView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class LatestPosts(StaticPageGeneratorByTask):
    spa_group = 'main'
    spa_page = 'posts'
    
    def sp_get(self, request):
        return render(request, 'posts/index.html', self.tc)





class PostView(BaseView):
    def get(self, request, code):
        posts = cache.get('cache_page__posts')
        post = posts.get(str(code))
        if post is None: raise Http404
        self.adapt_context(post)
        return render(request, 'posts/post.html', self.tc)

    def adapt_context(self, post):
        self.tc['title'] = post['title']
        self.tc['img'] = post['img']
        self.tc['text'] = format_html(post['text'])

 