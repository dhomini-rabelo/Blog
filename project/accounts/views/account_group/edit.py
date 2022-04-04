from random import randint
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.Support.forms.checks import check_is_logged
from django.shortcuts import render, redirect
from Support.Code.actions.Support.django.auth import change_password, logout, check_password
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions.Support.forms.utils import check_and_change_image_field
from Support.Code.actions.Support.django.messages.main import save_message
from Support.Code.actions.Support.utils.main import if_none
from Support.Code.actions._accounts.account_group.edit.email import change_user_email
from Support.Code.actions.shortcuts.form.main import get_form, save_form, delete_used_form
from Support.Code.actions.shortcuts.BlockForm.main import get_block_form, adapt_form_with_history, save_block_form, delete_base_block_form, delete_used_block_form
from Support.Code.actions.objects._accounts.account_group.edit.password import password_form, password_form_validation, password_message
from Support.Code.actions.objects._accounts.account_group.edit.email import new_email_form, new_email_form_validation
from Support.Code.actions.objects._accounts.account_group.edit.basic import basic_form_validation, basic_form, basic_form_message
from Support.Code.actions._accounts.account_group.edit.basic import save_user_basic_and_update_user_save
from Support.Code.actions.Support.django.messages.main import save_message, load_messages, load_message
from Support.Code.actions.objects._accounts.login_group.register import register_email_confirmation_form
from accounts.tasks.email import send_email_with_code




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
        self.tc['form'] = get_form(request, form_nickname='new_email', form_data=new_email_form)
        return render(request, 'accounts/account_group/edit/email.html', self.tc)
    
    def post(self, request):
        validation = validate_form(request.POST, new_email_form_validation)

        if validation['status'] == 'valid':
            delete_used_form(request, 'new_email')
            first_code = f'{randint(100000, 999999)}'
            request.session['new_email_codes'] = [first_code]
            request.session['new_email_process'] = validation['fields']['new_email']
            send_email_with_code.delay(validation['fields']['new_email'], first_code, 'new_email', request.get_host())            
            return redirect('new_email_confirmation')
            
        save_form(request, 'new_email', validation['fields'], validation['errors'])
        
        return redirect('account_group_edit_email')
    




class NewEmailConfirmationView(BaseView):
    
    def get(self, request):
        if self.is_not_verified(request): return redirect('account_page')
        self.tc['form'] = get_form(request, form_nickname='new_email_confirmation', form_data=register_email_confirmation_form)
        self.tc['email'] = request.session['new_email_process']
        self.tc['resend'] = if_none(request.session.get('new_email_codes_resend'), '')
        request.session['new_email_codes_resend'] = None
        return render(request, 'accounts/account_group/edit/new_email_confirmation.html', self.tc)
    
    def post(self, request):
        if self.is_not_verified(request): return redirect('account_page')
        
        if request.POST.get('code') in request.session['new_email_codes']:
            change_user_email(request, request.session['new_email_process'])
            logout(request)
            save_message(request, {'title': 'success_new_email', 'message': 'email alterado', 'type': 'success'})
            request.session['register_email_codes'] = None
            request.session['new_email_process'] = None
            return redirect('login')
        
        save_form(request, 'new_email_confirmation', {'code': ''}, {'code': 'Código inválido'})
        return redirect('new_email_confirmation')
    
    def is_not_verified(self, request):
        if (request.session.get('new_email_codes') is None) or (request.session.get('new_email_process') is None):
            return True
        return False
    
    
def send_new_email_for_new_email(request):
    if (request.session.get('new_email_codes') is None) or (request.session.get('new_email_process') is None):
        return redirect('account_page')
    new_code = f'{randint(100000, 999999)}'
    request.session['new_email_codes'].append(new_code)
    request.session['new_email_codes_resend'] = 'EMAIL FOI REENVIADO !!!'
    request.session.save()
    send_email_with_code.delay(request.session['new_email_process'], new_code, 'new_email_resend', request.get_host())
    return redirect('new_email_confirmation')
    
    

class EditPasswordAccountView(BaseView):

    def get(self, request):
        self.tc['form'] = get_form(request, form_nickname='password', form_data=password_form)
        return render(request, 'accounts/account_group/edit/password.html', self.tc)
    
    def post(self, request):
        validation = validate_form(request.POST, password_form_validation)
        check_password_validation = check_password(request, 'current_password')
        
        if validation['status'] == 'valid' and check_password_validation['status'] == 'valid':
            delete_used_form(request, 'password')
            change_password(request, 'new_password')
            logout(request)
            save_message(request, password_message)
            return redirect('login')

        save_form(request, 'password', validation['fields'], {**check_password_validation['errors'], **validation['errors']})
        return redirect('account_group_edit_password')
    