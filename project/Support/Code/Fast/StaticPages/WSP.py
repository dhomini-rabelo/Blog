from django.shortcuts import render
from Support.Code.actions.Support.django.views import BaseView


class WhenStaticPage(BaseView):

    def get(self, request):
        occasion = self.when(request)
        min_ = '/min' if self.use_min else ''
        
        if occasion:
            return render(request, f'static{min_}/WSP/{self.template_path}')
        else:
            return self.sp_get(request)