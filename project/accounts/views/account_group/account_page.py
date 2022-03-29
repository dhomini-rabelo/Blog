from Support.Code.actions.Support.django.messages.main import load_messages, save_message
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect

from Support.Code.actions.Support.utils.main import gets



class AccountView(BaseView):

    def get(self, request):
        if check_is_logged(request):
            user = request.session['user_save'].copy()
            self.tc['email'], self.tc['name'], self.tc['img'] = gets(user['data'], 'email', 'name', 'photo_url')
            self.tc['messages'] = load_messages(request, 'success_basic_form', 'success_login') 
            return render(request, 'accounts/account_group/account_page.html', self.tc)
        else:
            return render(request, 'accounts/account_group/no_login_account_page.html', self.tc)
            