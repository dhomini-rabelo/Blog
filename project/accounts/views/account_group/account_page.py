from Support.Code.actions.Support.django.messages.main import load_messages
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect



class AccountView(BaseView):

    def get(self, request):
        if check_is_logged(request):
            self.tc['user'] = request.session['user_save'].copy()
            self.tc['messages'] = load_messages(request, 'success_basic_form')
            return render(request, 'accounts/account_group/account_page.html', self.tc)
        else:
            return render(request, 'accounts/account_group/no_login_account_page.html', self.tc)
            