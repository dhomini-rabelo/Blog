from Support.Code.actions.Support.django.views import BaseView
from django.core.cache import cache
import json
from django.utils.html import format_html
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator






class GroupSpa(BaseView):
    
    # @method_decorator(cache_page(60 * 10)) 
    def get(self, request):
        static_pages_generated = cache.get('SPGT')
        self.tc['SPGT'] = json.dumps(static_pages_generated)
        self.tc['current_static_page'] = format_html(static_pages_generated[self.spa_group][self.spa_page])
        return self.sp_get(request)




class GroupChildrenSpa(BaseView):
    
    # @method_decorator(cache_page(60 * 10)) 
    def get(self, request, **kwargs):
        static_pages_generated = cache.get('SPGT')
        self.tc['SPGT'] = json.dumps(static_pages_generated)
        return self.sp_get(request, **kwargs)


