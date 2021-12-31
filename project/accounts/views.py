from Support.Code.actions._accounts.register import get_register_form, validate_register_form, save_register_form_errors, create_user, save_register_form_fields_values, delete_register_form_fields_values, show_success_message_for_user_register
from Support.Code.actions._accounts.login import get_login_form, load_messages_in_login_page, validate_login_form, login, save_login_form_errors, save_login_form_fields_values, save_server_error_of_login_process
from Support.Code.actions._accounts import save_javascript_use
from Support.Code.actions.Support.views import BaseView
from django.shortcuts import render, redirect



class RegisterView(BaseView):
    
    def get(self, request):
        self.tc['form'] = get_register_form(request)
        return render(request, 'accounts/register.html', self.tc)

    def post(self, request):
        validation = validate_register_form(request)

        if validation['status'] == 'valid':
            create_user(validation['fields'])
            delete_register_form_fields_values(request)
            show_success_message_for_user_register(request)
            return redirect('login')
        else:
            save_register_form_errors(request, validation['errors'])
            save_register_form_fields_values(request, validation['fields'])
            save_javascript_use(request)
            return redirect('register')




class LoginView(BaseView):

    def get(self, request):
        self.tc['form'] = get_login_form(request)
        self.tc['messages'] = load_messages_in_login_page(request)
        return render(request, 'accounts/login.html', self.tc)

    def post(self, request):
        login_validation = validate_login_form(request)

        if login_validation['status'] == 'valid':
            login_proccess = login(request)

            if login_proccess['status'] == 'valid':
                return redirect('latest_posts')
            else:
                save_login_form_errors(request, login_proccess['errors'])

        else:
            save_login_form_errors(request, login_validation['errors'])

        save_javascript_use(request)
        save_login_form_fields_values(request, login_validation['fields'])
        return redirect('login') 
            


class AccountView(BaseView):

    def get(self, request):
        return render(request, 'accounts/account_page.html', self.tc)
