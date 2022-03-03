from django.core.cache import cache
from random import randint
from Support.Code.actions.objects._accounts.login_group.register import register_form, register_form_validation, register_save_message, register_email_confirmation_form
from Support.Code.actions.objects._accounts.login_group.login import login_form, login_form_validation, login_obj, user_save, forgot_password_email_form, forgot_password_form, forgot_password_email_form_validation, forgot_password_form_validation
from Support.Code.actions._accounts.login_group.login import get_token_for_user
from Support.Code.actions._accounts.login_group.js_use import save_javascript_use
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.shortcuts.form.main import get_form, save_form, delete_used_form
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions.Support.django.auth import login, create_user_with_email, logout, create_login_save, validate_login
from Support.Code.actions.Support.django.messages.main import save_message, load_messages
from Support.Code.actions.Support.utils.main import gets, if_none
from django.shortcuts import render, redirect
from ..tasks.email import send_email_with_code, send_email_for_create_new_password
from Support.Code.actions.Support.django.auth import change_password
from Support.Code.actions.objects._accounts.account_group.edit.password import password_message



class RegisterView(BaseView):
    
    def get(self, request):
        self.tc['form'] = get_form(request, form_nickname='register', form_data=register_form)
        self.tc['js_use'] = request.session.get('js_use') if request.session.get('js_use') is not None else 'checked'
        return render(request, 'accounts/login_group/register.html', self.tc)

    def post(self, request):
        validation = validate_form(request.POST, register_form_validation)

        if validation['status'] == 'valid':
            request.session['register_data'] = validation['fields']
            first_code = f'{randint(100000, 999999)}'
            request.session['register_email_codes'] = [first_code]
            delete_used_form(request, 'register')
            send_email_with_code.delay(validation['fields']['email'], first_code, 'register')
            return redirect('register_email_confirmation')
        else:
            save_form(request, 'register', validation['fields'], validation['errors'])
            save_javascript_use(request)
            return redirect('register')



class RegisterEmailConfirmationView(BaseView):

    def get(self, request):
        if self.is_not_verified(request): return redirect('register')
        
        self.tc['form'] = get_form(request, form_nickname='register_email_confirmation', form_data=register_email_confirmation_form)
        self.tc['email'] = request.session['register_data']['email']
        self.tc['resend'] = if_none(request.session.get('register_email_codes_resend'), '')
        request.session['register_email_codes_resend'] = None
        return render(request, 'accounts/login_group/register_email_confirmation.html', self.tc)

    def post(self, request):
        if self.is_not_verified(request): return redirect('register')
        
        if request.POST.get('code') in request.session['register_email_codes']:
            create_user_with_email(request.session['register_data'])
            save_message(request, register_save_message)
            request.session['register_email_codes'] = None
            request.session['register_data'] = None
            return redirect('login')
        
        save_form(request, 'register_email_confirmation', {'code': ''}, {'code': 'Código inválido'})
        return redirect('register_email_confirmation')
    
    def is_not_verified(self, request):
        if (request.session.get('register_email_codes') is None) or (request.session.get('register_data') is None):
            return True
        return False
    
    
    
def send_new_email_for_register(request):
    if (request.session.get('register_email_codes') is None) or (request.session.get('register_data') is None):
        return redirect('register')
    new_code = f'{randint(100000, 999999)}'
    request.session['register_email_codes'].append(new_code)
    request.session['register_email_codes_resend'] = 'EMAIL FOI REENVIADO !!!'
    request.session.save()
    send_email_with_code.delay(request.session['register_data']['email'], new_code, 'register_resend')
    return redirect('register_email_confirmation')
    
    
    
    
    

class LoginView(BaseView):

    def get(self, request):
        self.tc['form'] = get_form(request, form_nickname='login', form_data=login_form)
        self.tc['js_use'] = request.session.get('js_use') if request.session.get('js_use') is not None else 'checked'
        self.tc['messages'] = load_messages(request, 'success_register', 'success_change_password')
        return render(request, 'accounts/login_group/login.html', self.tc)

    def post(self, request):
        login_validation = validate_form(request.POST, login_form_validation)
        login_proccess = validate_login(request, login_obj)

        if login_validation['status'] == 'valid' and login_proccess['status'] == 'valid':
            login(request, login_proccess['user'])
            delete_used_form(request, 'login')
            create_login_save(request, user_save)
            response = redirect('latest_posts')
            token = get_token_for_user(request.user.email)
            response.set_cookie('access_token', token['access'], max_age=60*60*24*3)
            response.set_cookie('refresh_token', token['refresh'], max_age=60*60*24*365)
            response.set_cookie('email', request.session['user_save']['email'], max_age=60*60*24*365)
            return response
        

        save_form(request, 'login', login_validation['fields'], {**login_proccess['errors'], **login_validation['errors']})
        save_javascript_use(request)
        return redirect('login') 
    
    

class ForgotPasswordEmailView(BaseView):
    
    def get(self, request):
        self.tc['form'] = get_form(request, form_nickname='forgot_password_email_form', form_data=forgot_password_email_form)
        return render(request, 'accounts/login_group/forgot_password_email.html', self.tc)
    
    def post(self, request):
        validation = validate_form(request.POST, forgot_password_email_form_validation)
        
        if validation['status'] == 'valid':
            token = get_token_for_user(validation['fields']['email'])['access']
            send_email_for_create_new_password.delay(validation['fields']['email'], token)
            return redirect('forgot_valid_email')
        
        save_form(request, 'forgot_password_email_form', validation['fields'], validation['errors'])
        return redirect('forgot_password_email')


def forgot_valid_email(request):
    return render(request, 'accounts/login_group/forgot_valid_email.html')


class ForgotPasswordView(BaseView):
    
    def get(self, request):
        validation = self.validate_get_data(request)

        if validation['status'] == 'invalid':
            self.tc['message'] = validation['error']
            return render(request, 'accounts/login_group/simple.html', self.tc)
            
        request.session['back'] = request.get_full_path()
        self.tc['form'] = get_form(request, form_nickname='forgot_password_form', form_data=forgot_password_form)
        return render(request, 'accounts/login_group/forgot_password.html', self.tc)
    
    
    def post(self, request):
        validation = validate_form(request.POST, forgot_password_form_validation)


        if validation['status'] == 'valid':
            change_password(request, 'new_password')
            save_message(request, password_message)
            return redirect('login')

        save_form(request, 'forgot_password_form', validation['fields'], validation['errors'])
        return redirect(request.session['back'])

    def validate_get_data(self, request):
        response = {'status': 'valid'}
        token, email = gets(request.GET, 'token', 'email')
        if (token is None) or (email is None):
            response['error'] = 'Informações inválidas'

        check = cache.get(f'create_new_password_to_{email}')
        if check is None:
           response['error'] = 'O cache expirou'
        elif check['token'] != token:
            response['error'] = 'token inválido'

        if response.get('error') is not None:
            response['status'] = 'invalid'

        return response
        


def logout_view(request):
    logout(request)
    return redirect('login')