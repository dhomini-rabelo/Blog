from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from Support.Code.Fast.StaticPages.SPGT import GroupSpa, GroupChildrenSpa
from django.core.cache import cache
from django.utils.html import format_html
from Support.Code.Fast.celery_beat.base import create_process_context
from Support.Code.actions.Support.django.messages.main import load_message, save_message
from Support.Code.actions.Support.django.views import BaseView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Post


class LatestPostsView(GroupSpa):
    spa_group = 'main'
    spa_page = 'posts'
    
    def sp_get(self, request):
        return render(request, 'posts/index.html', self.tc)





class PostView(GroupChildrenSpa): 
    def sp_get(self, request, code):
        posts = cache.get('cache_page__posts')
        post = posts.get(str(code))
        if post is None: raise Http404
        self.tc['current_cache_page'] = post
        return render(request, 'posts/post.html', self.tc)



class PostPreview(BaseView): 
    def get(self, request, code):
        post = get_object_or_404(Post, code=code)
        if post.author != request.user: return HttpResponseForbidden()
        self.tc = {
            'title': post.title,
            'img': post.img.url,
            'text': format_html(post.text)
        }
        return render(request, 'posts/preview.html', self.tc)

 