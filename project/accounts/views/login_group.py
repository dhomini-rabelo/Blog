from Support.Code.actions.objects._accounts.login_group.register import register_form, register_form_validation, register_save_message
from Support.Code.actions.objects._accounts.login_group.login import login_form, login_form_validation, login_obj, user_save
from Support.Code.actions._accounts.login_group.login import get_token_for_user
from Support.Code.actions._accounts.login_group.js_use import save_javascript_use
from Support.Code.actions.Support.django.views import BaseView
from Support.Code.actions.shortcuts.form.main import get_form, save_form, delete_used_form
from Support.Code.actions.Support.forms.main import validate_form
from Support.Code.actions.Support.django.auth import login, create_user_with_email, logout, create_login_save, validate_login
from Support.Code.actions.Support.django.messages.main import save_message, load_messages
from django.shortcuts import render, redirect
from ..tasks.email import send_email_with_celery


class RegisterView(BaseView):
    
    def get(self, request):
        self.tc['form'] = get_form(request, form_nickname='register', form_data=register_form)
        self.tc['js_use'] = request.session.get('js_use') if request.session.get('js_use') is not None else 'checked'
        return render(request, 'accounts/login_group/register.html', self.tc)

    def post(self, request):
        validation = validate_form(request.POST, register_form_validation)

        if validation['status'] == 'valid':
            create_user_with_email(validation['fields'])
            delete_used_form(request, 'register')
            save_message(request, register_save_message)
            return redirect('login')
        else:
            save_form(request, 'register', validation['fields'], validation['errors'])
            save_javascript_use(request)
            return redirect('register')




class LoginView(BaseView):

    def get(self, request):
        send_email_with_celery.delay('tyrundeyou@gmail.com')
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
            token = get_token_for_user(request)
            response.set_cookie('access_token', token['access'], max_age=60*60*24*3)
            response.set_cookie('refresh_token', token['refresh'], max_age=60*60*24*365)
            response.set_cookie('email', request.session['user_save']['email'], max_age=60*60*24*365)
            return response
        

        save_form(request, 'login', login_validation['fields'], {**login_proccess['errors'], **login_validation['errors']})
        save_javascript_use(request)
        return redirect('login') 
    
    
def logout_view(request):
    logout(request)
    return redirect('login')