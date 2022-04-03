from Support.Code.actions.Support.django.views import BaseView
from django.core.cache import cache






class GroupSpa(BaseView):
    
    def get(self, request):
        static_pages_obj = cache.get_many(['SPGT', 'SPGT_json'])
        self.tc['SPGT'] = static_pages_obj['SPGT_json']
        self.tc['current_static_page'] = static_pages_obj['SPGT'][self.spa_group][self.spa_page]
        return self.sp_get(request)




class GroupChildrenSpa(BaseView):
    
    def get(self, request, **kwargs):
        self.tc['SPGT'] = cache.get('SPGT_json')
        return self.sp_get(request, **kwargs)


