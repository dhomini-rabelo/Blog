from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect
from Support.Code.actions.Support.django.auth import change_password, logout
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions.Support.django.messages.main import save_message
from Support.Code.actions.shortcuts.form.main import get_form, save_form, delete_used_form
from Support.Code.actions.objects._accounts.account_group.edit.password import password_form, password_form_validation, password_message





class EditBasicAccountView(BaseView):

    def get(self, request):
        self.tc['user'] = request.user
        return render(request, 'accounts/account_group/edit/basic.html', self.tc)
    

class EditEmailAccountView(BaseView):

    def get(self, request):
        request.session.flush()
        return render(request, 'accounts/account_group/edit/email.html', self.tc)
    

class EditPasswordAccountView(BaseView):

    def get(self, request):
        self.tc['form'] = get_form(request, form_nickname='password', form_data=password_form)
        return render(request, 'accounts/account_group/edit/password.html', self.tc)
    
    def post(self, request):
        validation = validate_form(request.POST, password_form_validation)
        change_password_validation = change_password(request, 'current_password', 'new_password')
        
        if validation['status'] == 'valid' and change_password_validation['status'] == 'valid':
            delete_used_form(request, 'password')
            logout(request)
            save_message(request, password_message)
            return redirect('login')
        else:
            save_form(request, 'password', validation['fields'], {**change_password_validation['errors'], **validation['errors']})
        
        return redirect('account_group_edit_password')
    