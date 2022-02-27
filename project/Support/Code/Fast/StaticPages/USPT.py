from django.shortcuts import render
from Support.Code.actions.Support.django.views import BaseView
from django.core.cache import cache
from django.utils.html import format_html
import json



class UserStaticPageByTask(BaseView):

    def get(self, request):
        # USP recebe o user.mystaticpages
        user_static_pages_data = request.session['user_save']['USPT']
        self.tc['static_data'] = format_html(json.loads(user_static_pages_data[self.spa_page]))
        return self.sp_get(request)