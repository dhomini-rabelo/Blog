from django.http import Http404
from django.shortcuts import render
from Support.Code.Fast.StaticPages.SPGT import GroupSpa, GroupChildrenSpa
from django.core.cache import cache
from django.utils.html import format_html
from Support.Code.actions.Support.django.messages.main import load_message
from Support.Code.actions.Support.django.views import BaseView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class LatestPostsView(GroupSpa):
    spa_group = 'main'
    spa_page = 'posts'
    
    def sp_get(self, request):
        self.tc['message'] = load_message(request, 'success_login')
        return render(request, 'posts/index.html', self.tc)





class PostView(GroupChildrenSpa): 
    def sp_get(self, request, code):
        posts = cache.get('cache_page__posts')
        post = posts.get(str(code))
        if post is None: raise Http404
        self.tc['current_cache_page'] = post
        return render(request, 'posts/post.html', self.tc)

 