from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect



class AccountView(BaseView):

    def get(self, request):
        if check_is_logged(request):
            return render(request, 'accounts/account_group/account_page.html', self.tc)
        else:
            return render(request, 'accounts/account_group/no_login_account_page.html', self.tc)
            