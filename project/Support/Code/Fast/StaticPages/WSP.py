from django.shortcuts import render
from Support.Code.actions.Support.django.views import BaseView


class WhenStaticPage(BaseView):

    def get(self, request):
        occasion = self.when(request)
        min_ = '/min' if self.use_min else ''

        if hasattr(self, 'first') and (not request.session.get(self.template_path)):
            request.session[self.template_path] = True
            self.first(request)

        if hasattr(self, 'every'):
            self.every(request)
        
        if occasion:
            return render(request, f'static{min_}/WSP/{self.template_path}')
        else:
            return self.sp_get(request)