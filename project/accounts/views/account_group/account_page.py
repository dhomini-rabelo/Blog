from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect



class AccountView(BaseView):

    def get(self, request):
        self.tc['user'] = request.user
        return render(request, 'accounts/account_group/account_page.html', self.tc)