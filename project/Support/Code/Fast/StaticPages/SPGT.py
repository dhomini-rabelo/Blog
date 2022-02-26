from django.shortcuts import render
from Support.Code.actions.Support.django.views import BaseView
from django.core.cache import cache
import json
from django.utils.html import format_html



class StaticPageGeneratorByTask(BaseView):
    
    def get(self, request):
        static_pages_generated = cache.get('SPGT')
        self.tc['SPG'] = static_pages_generated.copy()
        self.tc['current_static_page'] = format_html(static_pages_generated[self.spa_group][self.spa_page])
        return self.sp_get(request)

