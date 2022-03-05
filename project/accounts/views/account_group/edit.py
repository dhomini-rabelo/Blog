from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect
from Support.Code.actions.Support.django.auth import change_password, logout, check_password
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions.Support.forms.utils import check_and_change_image_field
from Support.Code.actions.Support.django.messages.main import save_message
from Support.Code.actions.shortcuts.form.main import get_form, save_form, delete_used_form
from Support.Code.actions.shortcuts.BlockForm.main import get_block_form, adapt_form_with_history, save_block_form, delete_base_block_form, delete_used_block_form
from Support.Code.actions.objects._accounts.account_group.edit.password import password_form, password_form_validation, password_message
from Support.Code.actions.objects._accounts.account_group.edit.basic import basic_form_validation, basic_form, basic_form_message
from Support.Code.actions._accounts.account_group.edit.basic import save_user_basic_and_update_user_save
from Support.Code.actions.Support.django.messages.main import save_message, load_messages, load_message


class EditBasicAccountView(BaseView):

    def get(self, request):
        self.tc['user'] = request.session['user_save'].copy()
        adapt_form_with_history(basic_form, [{'src': self.tc['user']['data']['photo_url']}, {'value': self.tc['user']['data']['name']}])
        self.tc['form'] = get_block_form(request, 'ag_edit_basic', basic_form, True)
        return render(request, 'accounts/account_group/edit/basic.html', self.tc) 
    
    def post(self, request):
        validation = validate_form(request.POST, basic_form_validation)
        if validation['status'] == 'valid':
            save_user_basic_and_update_user_save(request)
            delete_used_block_form(request, 'ag_edit_basic')
            delete_base_block_form(request, 'ag_edit_basic')
            save_message(request, basic_form_message)
            return redirect('account_page')
            
        save_block_form(request, 'ag_edit_basic', request.POST, validation['errors'])
        return redirect('account_group_edit_basic')
    

class EditEmailAccountView(BaseView):

    def get(self, request):
        return render(request, 'accounts/account_group/edit/email.html', self.tc)
    

class EditPasswordAccountView(BaseView):

    def get(self, request):
        self.tc['form'] = get_form(request, form_nickname='password', form_data=password_form)
        return render(request, 'accounts/account_group/edit/password.html', self.tc)
    
    def post(self, request):
        validation = validate_form(request.POST, password_form_validation)
        check_password_validation = check_password(request, 'current_password')
        
        if validation['status'] == 'valid' and check_password_validation == 'valid':
            delete_used_form(request, 'password')
            change_password(request, 'new_password')
            logout(request)
            save_message(request, password_message)
            return redirect('login')
            
        save_form(request, 'password', validation['fields'], {**check_password_validation['errors'], **validation['errors']})
        
        return redirect('account_group_edit_password')
    