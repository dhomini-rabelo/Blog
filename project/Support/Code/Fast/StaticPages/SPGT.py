from Support.Code.actions.Support.django.views import BaseView
from django.core.cache import cache
# import json
# from django.utils.html import format_html
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator






class GroupSpa(BaseView):
    
    # @method_decorator(cache_page(60 * 10)) 
    def get(self, request):
        static_pages_obj = cache.get_many(['SPGT', 'SPGT_json'])
        self.tc['SPGT'] = static_pages_obj['SPGT_json']
        self.tc['current_static_page'] = static_pages_obj['SPGT'][self.spa_group][self.spa_page]
        return self.sp_get(request)




class GroupChildrenSpa(BaseView):
    
    # @method_decorator(cache_page(60 * 10)) 
    def get(self, request, **kwargs):
        self.tc['SPGT'] = cache.get('SPGT_json')
        return self.sp_get(request, **kwargs)


